from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from PIL import Image
import time
import sys


prog_start = time.time()

# MEIPATH for Mac:
ROOT_DIR = os.path.join(sys._MEIPASS, "../../..")
# Path for Windows:
# ROOT_DIR = os.path.join(os.getcwd(), "../../..")
SYSTEM_DIR = os.path.join(ROOT_DIR, "System Files")
SSHOTS_DIR = os.path.join(ROOT_DIR, "Screenshots")

urls = {
    "fb": "https://www.facebook.com/ReutersUK/posts/3205669936109807?__xts__%5B0%5D=68.ARAtP3rnyABij3uDx2hCUMI-EDea6i6hM3Kzv2ZwvK9zFGMq-srkzMdSl-5Kt-VajlMWTqEtVXYE1UULm5mf5DHdhm7ciJM5x-47Nutei6F6z6tfphcZGTnNUwxOQZdvDNvBVfp3CZfw_6Li1UnhopnYyZ57xXXw1YiwVZq_j7CMldgbJUQhbDUM5RU_KQXoFiVJ0Lkz65hZ_EzQQApDk5Jsak6GbSZo0LgGSmQPLL8baQ_O_HqNISYH-J5kRq5zxaQzUXZAT_nV2Fwr7Z4_MvYydsDLLRSdctVXT4HA8NGib4dppHR6uWH2menkeYPJBVjAUwYPUaDWgm0-VSp9cJMuBQ&__tn__=-R",
    "twtr": "https://twitter.com/Reuters/status/1240036547652726784",
    "ig": "https://www.instagram.com/p/B934JlLjU89/",
    "lin": "https://www.linkedin.com/posts/reuters2_coronavirus-activity-6646028828793716738-CN0Y",
    "yt": "https://www.youtube.com/watch?v=AL9ru777zBI",
}
driver = webdriver.Chrome(os.path.join(SYSTEM_DIR, "chromedriver 2"))

for i in range(3):
    loop_start = time.time()
    for pf, url in urls.items():
        driver.get(url)
        driver.maximize_window()
        driver.save_screenshot(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_0SEC.png"))
        time.sleep(1)
        driver.save_screenshot(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_1SEC.png"))
        time.sleep(1)
        driver.save_screenshot(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_2SEC.png"))
        time.sleep(1)
        driver.save_screenshot(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_3SEC.png"))

        if i == 0:
            im = Image.open(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_0SEC.png"))
            x1 = 0  # over from upper left
            y1 = 100  # down for upper left
            x2 = im.width
            y2 = im.height
            cropped = im.crop((x1, y1, x2, y2))
            cropped.save(os.path.join(SSHOTS_DIR, f"{pf}_t{i}_0SEC_crpd.png"))
        with open(os.path.join(SSHOTS_DIR, "log.txt"), "a") as log:
            log.write(f"Loop {i}, {pf} duration: {time.time() - loop_start}\n")

driver.quit()

with open(os.path.join(SSHOTS_DIR, "log.txt"), "a") as log:
    log.write(f"Program duration: {time.time() - prog_start}\n")
