import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import ChromeType
import time


def chrome():
    return webdriver.Chrome(ChromeDriverManager().install())

def chromium():
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

def firefox():
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())

def ie():
    return webdriver.Ie(IEDriverManager().install())

def edge():
    return webdriver.Edge(EdgeChromiumDriverManager().install())


def initiate():
    driver = None
    
    browsers = [chrome,chromium,firefox,ie,edge]
    
    for browser in browsers:
        try:
            driver = browser()
            if driver:
                break
        except:
            continue

    return driver


def get_header():
    driver = initiate()
    header_text = None
    try:
        web = driver.get('https://www.grousemountain.com/')
        time.sleep(3)
        header = driver.find_element_by_xpath(("//div[@id='site_wide_alert']"))
        header_text = header.text
    finally:
        terminate(driver)
        if driver:
            return header_text


def terminate(driver):
    driver.quit()


if __name__ == '__main__':
    test_header = get_header()
    print(f'header: {test_header}')
