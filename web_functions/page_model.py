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


def initiate():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except ValueError:
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    except ValueError:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    except ValueError:
        driver = webdriver.Ie(IEDriverManager().install())
    except ValueError:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    return driver


def get_header():
    driver = initiate()
    header_text = None
    try:
        driver.get('https://www.grousemountain.com/')
        time.sleep(3)
        header = driver.find_element_by_xpath(("//div[@id='site_wide_alert']"))
        header_text = header.text
    finally:
        terminate(driver)
        return header_text


def terminate(driver):
    driver.quit()


if __name__ == '__main__':
    test_header = get_header()
    print(f'header: {test_header}')
