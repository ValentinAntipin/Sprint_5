from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators
import time

class PersonalAccount:

    def test_navigate_to_personal_account(self, driver):
        # Переход на главную страницу
        driver.get(f'{Config.URL}')  # URL главной страницы

        # Находим и кликаем на кнопку "Личный кабинет"
        personal_account_button = driver.find_element(*Mestolocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на страницу личного кабинета
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('account/profile')  # URL страницы личного кабинета
        )

        # Проверяем, что находимся на странице личного кабинета
        assert "Личный кабинет" in driver.title, "Не перешли на страницу личного кабинета"
