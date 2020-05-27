from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def initiate():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def get_header():
    driver = initiate()
    header = None
    try:
        driver.get('https://www.grousemountain.com/')
        header = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "container_text_1161242")))
    finally:
        terminate(driver)
        return header


def terminate(driver):
    driver.quit()


if __name__ == '__main__':
    test_header = get_header().text
    print(f'header: {test_header}')
