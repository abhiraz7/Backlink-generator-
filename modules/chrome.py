

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager

def driver(baseurl):
    options = webdriver.ChromeOptions()
    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)

    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(baseurl)
    driver.implicitly_wait(10)

    return driver

class parent:
    def dad(self):
        print("dad")

    def __init__(self):
        super().__init__()
        print()

    def __new__(cls):
        return super().__new__(cls)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def mom(self):
        print('Mon')



