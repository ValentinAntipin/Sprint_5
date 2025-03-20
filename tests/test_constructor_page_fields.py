from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators

class TestConstructorNavigation:

    def test_navigate_to_buns_section(self, driver):
        # Переход на страницу конструктора
        driver.get(f'{Config.URL}')

        # Ожидаем загрузки страницы конструктора
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL страницы конструктора
        )

        # Находим и кликаем на кнопку "Булки"
        buns_button = driver.find_element(*Mestolocators.BUNS_BUTTON)
        buns_button.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на раздел "Булки"
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL раздела булок
        )

        # Проверяем, что находимся в разделе булок
        assert "Булки" in driver.title, "Не перешли на раздел «Булки»"

    def test_navigate_to_sauces_section(self, driver):
        # Переход на страницу конструктора
        driver.get(f'{Config.URL}/span')

        # Ожидаем загрузки страницы конструктора
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL страницы конструктора
        )

        # Находим и кликаем на кнопку "Соусы"
        sauces_button = driver.find_element(*Mestolocators.SAUCES_BUTTON)
        sauces_button.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на раздел "Соусы"
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL раздела соусов
        )

        # Проверяем, что находимся в разделе соусов
        assert "Соусы" in driver.title, "Не перешли на раздел «Соусы»"

    def test_navigate_to_toppings_section(self, driver):
        # Переход на страницу конструктора
        driver.get(f'{Config.URL}/span')

        # Ожидаем загрузки страницы конструктора
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL страницы конструктора
        )

        # Находим и кликаем на кнопку "Начинки"
        toppings_button = driver.find_element(*Mestolocators.TOPPINGS_BUTTON)
        toppings_button.click()

        # Ожидаем, что страница обновится, и проверяем, что перешли на раздел "Начинки"
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.url_contains('/span')  # URL раздела начинок
        )

        # Проверяем, что находимся в разделе начинок
        assert "Начинки" in driver.title, "Не перешли на раздел «Начинки»"
