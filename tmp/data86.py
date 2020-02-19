# main_prot.py

import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import ezodf
import shutil
import sys
import json
from shutil import copyfile

program_start_time = time.time()

# Program executes in 'System Files' directory
ROOT_DIR = os.path.join(sys._MEIPASS, "../../..")  # Autofocus Root Folder
DEALERSHIP_DIR = os.path.join(ROOT_DIR, "Dealership Directories")
if "Dealership Directories" not in os.listdir(ROOT_DIR):
    os.mkdir(DEALERSHIP_DIR)
if "Archives" not in os.listdir():
    os.mkdir("Archives")

SYSTEM_DIR = os.path.join(ROOT_DIR, "System Files")
DEALERSHIP_LIST = os.path.join(SYSTEM_DIR, "dealerships.txt")
ARCHIVES_DIR = os.path.join(SYSTEM_DIR, "Archives")
ARCHVE_LOG = os.path.join(ARCHIVES_DIR, "log.log")
EXTENSIONS = ["xls", "xlsx", "csv", "ods"]
DEALERS = []
with open(DEALERSHIP_LIST, "r") as dealerships:
    for dealer in dealerships:
        DEALERS.append(dealer.strip("\n\t"))

copyfile(
    os.path.join(SYSTEM_DIR, "af_prot_secret.json"),
    os.path.join(os.getcwd(), "af_prot_secret.json"),
)

## **** Update dealer_sheets.json based on Dealership Directories


class Data:
    def __init__(self, source_file):
        self.source_file = source_file

    def parse_source_file(self, gs=False):

        print(f"In {os.getcwd()} Located {self.source_file}")
        print("Raw data recieved")

        def parse_ods(source_file):
            doc = ezodf.opendoc(source_file)

            sheet = doc.sheets[0]
            df_dict = {}
            for i, row in enumerate(sheet.rows()):
                # row is a list of cells
                # assume the header is on the first row
                if i == 0:
                    # columns as lists in a dictionary
                    df_dict = {cell.value: [] for cell in row}
                    # create index for the column headers
                    col_index = {j: cell.value for j, cell in enumerate(row)}
                    continue
                for j, cell in enumerate(row):
                    # use header instead of column index
                    df_dict[col_index[j]].append(cell.value)
            self.df = pd.DataFrame(df_dict)
            return self.df

        print(f"FILENAME: {self.source_file}")
        self.file_name = self.source_file.split(".")[0]
        file_ext = self.source_file.split(".")[1]
        if file_ext == "ods":
            self.df = parse_ods(self.source_file)
        elif file_ext == "csv":
            self.df = pd.read_csv(self.source_file)
        elif file_ext == "xls" or "xlsx":
            try:
                self.df = pd.read_excel(self.source_file)
            except:
                self.df = pd.read_html(self.source_file)
                self.df = pd.concat(self.df)
        print("Data Frame created from source file")

        # Arrange DataFrame
        if "Make" and "Model" in self.df:
            self.df["Make & Model"] = self.df["Make"].map(str) + " " + self.df["Model"]
        if "Year" and "Make & Model" in self.df:
            self.df["Year"] = self.df["Year"].fillna(0).astype(np.int64)
            self.df["Vehicle"] = (
                self.df["Year"].map(str) + " " + self.df["Make & Model"]
            )
        if "Stock" in self.df:
            self.df.rename(columns={"Stock": "Stock #"}, inplace=True)
        if "Days In Stock" in self.df:
            self.df.rename(columns={"Days In Stock": "Age"}, inplace=True)
        if "Status" not in self.df:
            self.df["Status"] = ""

        if "Photos" not in self.df:
            self.df["Photos"] = ""
        self.df["Notes"] = ""
        ##### Age[0] Vehicle[1] Stock #[2] VIN[3] Photos[4] Status[5] Notes[6]
        if gs == True:
            self.df = self.df[
                [
                    "Age",
                    "VIN",
                    "Stock #",
                    "Vehicle",
                    "Photos",
                    "Status",
                    "Notes",
                    "Rooftop",
                ]
            ]
        elif gs == False:
            self.df = self.df[
                ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes"]
            ]
        ## WRITE EXCEPTION FOR GARLYN SHELTON TO DISPLAY ROOFTOPS ******

        # Need to see if theres an AGE limit to being listed in order
        self.df = self.df.sort_values(by="Age", ascending=False)
        print("Data Frame arranged and ready to be converted to spreadsheet...")
        return self.df

    def convert_sheet(self):

        self.df = self.parse_source_file()
        self.file_name = self.source_file.split(".")[0]
        # Convert DataFrame to spreadsheet & CSV
        self.df.to_csv(str(self.file_name + "_DF.csv"), index=False)
        # xls
        writer = pd.ExcelWriter(str(self.file_name + "_DF.xlsx"))
        self.df.to_excel(writer, index=False, sheet_name="In Progress")
        # *** NEED TO FIGURE OUT HOW NOT TO ADD DF TO COMPLETED TAB ***
        self.df.to_excel(writer, index=False, sheet_name="Completed")
        workbook = writer.book
        worksheet = writer.sheets["In Progress"]

        align_left_format = workbook.add_format()
        align_left_format.set_align("left")
        ## Adjust height of Row 2

        worksheet.set_column("A:A", 6, align_left_format)
        worksheet.set_column("B:B", 25, align_left_format)
        worksheet.set_column("C:C", 12, align_left_format)
        worksheet.set_column("D:D", 30, align_left_format)
        worksheet.set_column("E:E", 8, align_left_format)
        worksheet.set_column("F:F", 18, align_left_format)
        worksheet.set_column("G:G", 25, align_left_format)

        writer.save()
        print("Production file packaging finished")
        print(self.file_name + " ready to be shipped")


def file_crawler():
    """
    The file crawler currently relies on data86.Data to change
    directories in and out so that the secrets file can be used.
    So that means that file_crawler and data86.Data rely on each
    other to get in and out of directories. Advised to clean this
    up.
    """
    counter = 0
    print(f"***** IN file_crawler() cwd: {os.getcwd()}")
    print("Directories: ")
    source_directories = os.listdir(DEALERSHIP_DIR.strip("\t"))
    print(source_directories)
    DEALER_SHEETS = os.path.join(SYSTEM_DIR, "dealer_sheets.json")
    with open(DEALER_SHEETS, "r") as read_file:
        parsed_dealer_sheets = json.load(read_file)
    for directory in source_directories:
        if directory in DEALERS:
            print(f"___________ Trying {directory} ___________")
            print(
                f"Contains: {str(os.listdir(os.path.join(DEALERSHIP_DIR, directory)))}"
            )

            production_sheet = parsed_dealer_sheets[0][directory]
            for local_file in os.listdir(os.path.join(DEALERSHIP_DIR, directory)):
                if local_file.split(".")[1] in EXTENSIONS:
                    print(f"***** IN file_crawler() cwd: {os.getcwd()}")
                    file_sync(local_file, directory, production_sheet)
                # os.chdir(directory.strip("\t"))
                else:
                    continue
            counter += 1
        else:
            continue
    print(f"Completed {counter} Dealership Files")
    print("Parsing Complete")


"""
****** WRITE EXCEPTION FOR GARLYN SHELTON TO DISPLAY ROOFTOPS ******
"""


def file_sync(local_file, directory, production_sheet):
    """ Both the LOCAL and IMPORTED sheets have the same name and 
        file structure. Currently, the program doesn't differenciate
        between the two to ensure file name continuity. """

    time_now = time.localtime()
    start_time = time.strftime("%m%d%Y%H%M%S", time_now)
    event_time = time.strftime("%m-%d-%Y, %H:%M:%S", time_now)

    SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "af_prot_secret.json", SCOPE
    )
    client = gspread.authorize(creds)

    os.chdir(os.path.join(DEALERSHIP_DIR, directory))

    ## IMPORTED SHEETS FILE
    print("Importing spreadsheet data frame from PRODUCTION FILE")
    imported_sheet = client.open(production_sheet).sheet1
    imported_sheet_df = imported_sheet.get_all_records()
    print(f"LENGTH OF IMPORTED_SHEET: {len(imported_sheet_df)}")

    print("Importing and parsing LOCAL source file")
    imported_df = pd.DataFrame(imported_sheet_df)
    if "Garlyn Shelton Used" not in directory:
        imported_df = imported_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes"]
        ]
    elif "Garlyn Shelton Used" in directory:
        imported_df = imported_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes", "Rooftop"]
        ]
    # Archving
    logFile = start_time + directory + "_imported.csv"
    archive_logger(imported_df, logFile, event_time, event="imported")
    print("Imported dataframe logged and archived")

    ## LOCAL FILE
    if "Garlyn Shelton Used" not in directory:
        local_df = Data(local_file).parse_source_file()
    elif "Garlyn Shelton Used" in directory:
        local_df = Data(local_file).parse_source_file(gs=True)

    # Archiving
    logFile = start_time + directory + "_local.csv"
    archive_logger(local_df, logFile, event_time, event="local")
    print("Local dataframe logged and archived")

    ## JOINED DF
    print("Loading IMPORTED dataframe")
    joined_df = pd.concat([imported_df, local_df]).drop_duplicates(
        subset=["VIN"], keep=False
    )
    if "Garlyn" not in directory:
        joined_df = joined_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes"]
        ]
    elif "Garlyn" in directory:
        joined_df = joined_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes", "Rooftop"]
        ]
    joined_df.fillna("", inplace=True)
    print("Merging LOCAL and IMPORTED dataframes...")
    rows = joined_df.values.tolist()
    print(f"NUMBER OF ROWS TO APPEND: {len(rows)}")
    print("Updating live Production Google Sheets...")
    for row in rows:
        # print(row)
        try:
            imported_sheet.insert_row(row, len(imported_df) + 2)
            time.sleep(1.5)
        except Exception as e:
            if str(e).find("RESOURCE_EXHAUSTED") > -1:
                print("resource exhausted...")
                time.sleep(10)
    # Archiving
    logFile = start_time + directory + "_cleaned.csv"
    archive_logger(joined_df, logFile, event_time, event="cleaned")
    print("Joined dataframe logged and archived")

    # Archiving Live Sheet
    updated_sheet = client.open(production_sheet).sheet1
    updated_sheet_df = updated_sheet.get_all_records()
    updated_df = pd.DataFrame(updated_sheet_df)
    if "Garlyn" not in directory:
        updated_df = updated_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes"]
        ]
    elif "Garlyn" in directory:
        updated_df = updated_df[
            ["Age", "VIN", "Stock #", "Vehicle", "Photos", "Status", "Notes", "Rooftop"]
        ]
    logFile = start_time + directory + "_updated.csv"
    archive_logger(updated_df, logFile, event_time, event="updated")
    print("Live production Google Sheet updated, logged and archived")
    os.remove(local_file)
    os.chdir(SYSTEM_DIR)


def archive_logger(dataframe, log_file_name, event_time, event):
    """
    local_source_file, imported_sheets_file, cleaned_dataframe, updated_sheets_file
    """

    if event == "imported":
        action, location = "Imported", "from Google Sheets"
    elif event == "local":
        action, location = "Parsed", "from Inventory Platform"
    elif event == "cleaned":
        action, location = "Cleaned dataframe:", "from local file"
    elif event == "updated":
        action, location = "Updated Sheet: ", "to Google Sheets"
    else:
        raise ValueError(
            "'event' parameter must be set to 'imported', 'local', 'cleaned', or 'updated'"
        )
    dataframe.to_csv(log_file_name)
    shutil.move(log_file_name, ARCHIVES_DIR)
    log_event = f"{event_time}    {action} {log_file_name} {location}\n"
    with open(ARCHVE_LOG, "a") as logger:
        logger.write(log_event)


def verify_dir():
    """Verify or create dealership directories for raw photo report"""
    print("Verifying Dealership Directories...")
    subfolders = os.listdir(DEALERSHIP_DIR)

    for _ in DEALERS:
        if _.strip("\t") not in subfolders:
            os.chdir(DEALERSHIP_DIR)
            os.mkdir(_)
            print(f"Making a directory for {_}")
        else:
            continue


def check_pip_freeze_for_dependancies_install():
    pass


verify_dir()
file_crawler()
print(f"Program completed in {time.time() - program_start_time} seconds")
# if __name__ == '__main__':
#     data = Data('PhotoReport-2-11-2020.xls')
#     data.convert_sheet()
