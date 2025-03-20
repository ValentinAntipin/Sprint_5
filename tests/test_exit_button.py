from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators

class TestLogout:

    def test_logout_from_personal_account(self, driver):
        # Переход на страницу личного кабинета
        driver.get(f'{Config.URL}/account/profile')  # URL личного кабинета

        # Ожидаем, что страница загрузится, и проверяем, что находимся на личном кабинете
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/account/profile')  # URL страницы личного кабинета
        )

        # Проверяем, что находимся на странице личного кабинета
        assert "Личный кабинет" in driver.title, "Не на странице личного кабинета"

        # Находим и кликаем на кнопку "Выйти"
        logout_button = driver.find_element(*Mestolocators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидаем, что после выхода с нас перенаправит на главную страницу
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('')  # URL главной страницы после выхода
        )

        # Проверяем, что находимся на главной странице
        assert "Главная" in driver.title, "Не перешли на главную страницу после выхода"

        # Проверяем, что на главной странице есть кнопка "Войти"
        login_button = driver.find_element(*Mestolocators.LOGIN_BUTTON)
        assert login_button.is_displayed(), "Кнопка «Войти в аккаунт» не отображается после выхода"
