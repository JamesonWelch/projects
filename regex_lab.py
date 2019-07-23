import re
import requests
from bs4 import BeautifulSoup


def phone():
    general_number = str(input("Input a number: "))

    regex = re.compile(r"[0-9]{3}-[0-9]{3}-[0-9]{4}")

    if regex.search(general_number) == None:
        print("Doesn't Validate!")
    else:
        print("Verified Number!")


def ssn():
    ssn_checker = str(input("Input a SSN: "))

    regex_ssn = re.compile(r"[0-9]{3}-[0-9]{2}-[0-9]{4}")

    if regex_ssn.search(ssn_checker) == None:
        print("{} is an invalid Social Security Number!".format(ssn_checker))
    else:
        print("{} is a valid Social Security Numner!".format(ssn_checker))


def email():
    email_checker = str(input("Input email: "))
    regex_email = re.compile(
        r"[a-zA-Z0-9'\_'].{0,1}['\+'a-zA-Z0-9_]@{1}([a-zA-Z0-9'\\']'\.'{0,1}[a-zA-Z].{1}[a-zA-Z{2+}]|\[[[0-9]{3}.[0-9]{3}.[0-9]{1,3}.[0-9]{1,3}]\])"
    )

    if regex_email.search(email_checker) == None:
        print("{} is an invalid email address.".format(email_checker))
    else:
        print("{} is a valid email.".format(email_checker))


def lyrics():
    req = requests.get("https://www.lyrics.com/lyric/1268623/Tool/Forty+Six+%26+2")

    soup = BeautifulSoup(req.text, "html.parser")
    lyrics = soup.find("pre", {"id": "lyric-body-text"}).text

    vowels = re.compile("[aeiouAEIOU]")
    vowels_list = vowels.findall(lyrics)
    # consonants = re.compile("![aeiouAEIOU]")
    cons = len(lyrics) - len(vowels_list)

    print("There are " + str(len(lyrics)) + " total letters.")
    print("With " + str(len(vowels_list)) + " vowels.")
    print("And " + str(cons) + " consonants.")


def ferrari():
    req = requests.get("https://en.wikipedia.org/wiki/Ferrari")
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", {"class": "mw-body"}).text

    fer_search = re.compile("Ferrari")
    fer_list = fer_search.findall(txt)

    print(len(fer_list))


ferrari()
