import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import argparse
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Comment the list if you want to disable few type of device
mobile_emulation = [
    "BlackBerry Z30",
    "Galaxy Note 3",
    "Kindle Fire HDX",
    "LG Optimus L70",
    "Laptop with HiDPI screen",
    "Laptop with MDPI screen",
    "Laptop with touch",
    "Microsoft Lumia 550",
    "Microsoft Lumia 950",
    "Nexus 10",
    "Nexus 4",
    "Nexus 5",
    "Nexus 6",
    "Nexus 6P",
    "Nexus 7",
    "Nokia Lumia 520",
    "Nokia N9",
    "iPad Mini",
    "iPhone 4",
    "Galaxy S5",
    "Pixel 2",
    "Pixel 2 XL",
    "iPhone 5/SE",
    "iPhone 5/SE",
    "iPhone 6/7/8",
    "iPhone 6/7/8 Plus",
    "iPhone X",
    "iPad",
    "iPad Pro"]


def start_test(url):
    for i in mobile_emulation:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "mobileEmulation", {"deviceName": i})
        driver = webdriver.Chrome(
            executable_path='../driver/chromedriver',
            options=chrome_options)

        driver.get(url)
        time.sleep(5)
        driver.save_screenshot('test/%s.png' % i)
        driver.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="Please input url to test")
    args = vars(parser.parse_args())
    start_test(args['url'])
