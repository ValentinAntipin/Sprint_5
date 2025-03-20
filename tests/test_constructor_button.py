from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators
import time

class TestNavigation:
    def test_navigate_from_personal_account_to_constructor(self, driver):
        # Переход в личный кабинет
        driver.get(f'{Config.URL}/account/profile')  # URL личного кабинета

        # Находим и кликаем на кнопку "Конструктор"
        constructor_button = driver.find_element(*Mestolocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на страницу конструктора
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('')  # URL страницы конструктора
        )

        # Проверяем, что находимся на странице конструктора
        assert "Конструктор" in driver.title, "Не перешли на страницу конструктора"

    def test_navigate_from_personal_account_to_constructor_by_logo(self, driver):
        # Переход в личный кабинет
        driver.get(f'{Config.URL}/account/profile')  # URL личного кабинета

        # Находим и кликаем на логотип Stellar Burgers
        logo = driver.find_element(*Mestolocators.LOGO)
        logo.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на страницу конструктора
        WebDriverWait(driver, Config.TIMEOUT).until(
        EC.url_contains('')  # URL страницы конструктора
        )


        # Проверяем, что находимся на странице конструктора
        assert "Конструктор" in driver.title, "Не перешли на страницу конструктора"