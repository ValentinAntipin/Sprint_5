import pytest
from selenium import webdriver
from src.config import Config


def browser_settings():
    crome_options = webdriver.ChromeOptions()
    width, height = Config.RESOLUTION
    chrome_options.add_argument(f'--windows-size={width},{height}')
    return chrome_options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()



