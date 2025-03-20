from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators
from src.helpers import get_sign_up_data
import time


class TestLogin:

    def test_login_button_from_home_page(self, driver):
        # Переход на главную страницу
        driver.get(f'{Config.URL}')  # URL главной страницы

        # Нажимаем на кнопку "Войти в аккаунт"
        login_button = driver.find_element(*Mestolocators.LOGIN_BUTTON)
        login_button.click()

        # Ожидаем перехода на страницу входа
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/login')  # URL страницы входа должен содержать /login
        )

        # Проверяем, что находимся на странице входа
        assert "Вход" in driver.title, "Не перешли на страницу входа"

    def test_login_button_from_personal_account(self, driver):
        # Переход на главную страницу или страницу личного кабинета
        driver.get(f'{Config.URL}')  # URL страницы личного кабинета

        # Нажимаем на кнопку "Личный кабинет"
        personal_account_button = driver.find_element(*Mestolocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        # Ожидаем перехода на страницу личного кабинета
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/account/profile')  # URL личного кабинета
        )

        # Проверяем, что находимся на странице личного кабинета
        assert "Личный кабинет" in driver.title, "Не перешли на страницу личного кабинета"

    def test_login_button_in_registration_form(self, driver):
        # Переход на страницу регистрации
        driver.get(f'{Config.URL}/register')

        # Нажимаем на кнопку "Войти" в форме регистрации
        login_button = driver.find_element(*Mestolocators.LOGIN_BUTTON_IN_REGISTRATION)
        login_button.click()

        # Ожидаем перехода на страницу входа
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/login')  # URL страницы входа
        )

        # Проверяем, что находимся на странице входа
        assert "Вход" in driver.title, "Не перешли на страницу входа"

    def test_login_button_in_forgot_password_form(self, driver):
        # Переход на страницу восстановления пароля
        driver.get(f'{Config.URL}/forgot-password')

        # Нажимаем на кнопку "Войти" в форме восстановления пароля
        login_button = driver.find_element(*Mestolocators.LOGIN_BUTTON_IN_PASSWORD_RECOVERY)
        login_button.click()

        # Ожидаем перехода на страницу входа
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/login')  # URL страницы входа
        )

        # Проверяем, что находимся на странице входа
        assert "Вход" in driver.title, "Не перешли на страницу входа"
