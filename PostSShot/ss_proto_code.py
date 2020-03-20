from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,600")
driver = webdriver.Chrome(
    chrome_options=options,
    executable_path=r"C:\Utility\BrowserDrivers\chromedriver.exe",
    service_args=["--log-path=./Logs/DubiousDan.log"],
)
driver.get("http://google.com/")
print("Headless Chrome Initialized")
print(driver.get_window_size())
driver.set_window_size(1920, 1080)
size = driver.get_window_size()
print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))
driver.quit()
