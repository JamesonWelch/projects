from requests import (
    RequestException,
    HTTPError,
    ConnectionError,
    URLRequired,
    TooManyRedirects,
)
from bs4 import BeautifulSoup
import requests


def download(url, tries=3):

    headers = requests.utils.default_headers()
    headers.update(
        {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
        }
    )
    try:
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.text, "lxml")
    except (
        RequestException,
        HTTPError,
        ConnectionError,
        URLRequired,
        TooManyRedirects,
    ) as e:
        print("Download error: {}".format(e))
        if tries > 0:
            return download(url, tries - 1)
    return soup
