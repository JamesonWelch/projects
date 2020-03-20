from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from PIL import Image
import time

# ROOT_DIR = os.path.join(os.getcwd(), "../../..")
ROOT_DIR = os.path.join(os.getcwd(), "..")
SSHOTS_DIR = os.path.join(ROOT_DIR, "Screenshots")

driver = webdriver.Chrome("/Users/jamesonwelch/Downloads/chromedriver 2")

driver.get(
    "https://www.facebook.com/ReutersUK/posts/3205669936109807?__xts__%5B0%5D=68.ARAtP3rnyABij3uDx2hCUMI-EDea6i6hM3Kzv2ZwvK9zFGMq-srkzMdSl-5Kt-VajlMWTqEtVXYE1UULm5mf5DHdhm7ciJM5x-47Nutei6F6z6tfphcZGTnNUwxOQZdvDNvBVfp3CZfw_6Li1UnhopnYyZ57xXXw1YiwVZq_j7CMldgbJUQhbDUM5RU_KQXoFiVJ0Lkz65hZ_EzQQApDk5Jsak6GbSZo0LgGSmQPLL8baQ_O_HqNISYH-J5kRq5zxaQzUXZAT_nV2Fwr7Z4_MvYydsDLLRSdctVXT4HA8NGib4dppHR6uWH2menkeYPJBVjAUwYPUaDWgm0-VSp9cJMuBQ&__tn__=-R"
)

time.sleep(1)
driver.save_screenshot(os.path.join(SSHOTS_DIR, "R.png"))
driver.quit()


im = Image.open(os.path.join(SSHOTS_DIR, "R.png"))
im.show()
down = 205
from_left = 530
From_right = 785
