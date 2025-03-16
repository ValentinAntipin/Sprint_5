from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.config import Config
from src.locators import MestoLocators
from src.helpers import get_sign_up_data

class TestRegisration:

    def get_sign_up_data(self, driver):
        assert driver.current_url == f'{Config.URL}/sigin', "Не правилиный URL"

    def test_signup(self, driver):
        driver.get(f'{Config.URL}/signup')
        email_data, password_data = get_sign_up_data()







    driver.quit()