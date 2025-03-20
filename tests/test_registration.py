from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.locators import Mestolocators
from src.helpers import get_sign_up_data


class TestRegisration:

    def get_sign_up_data(self, driver):
        assert driver.current_url == f'{Config.URL}/sigin', "Не правельный URL"

    def test_signup_succesful(self, driver):
        driver.get(f'{Config.URL}/register')

        # Получаем данные для регистрации
        name_data, email_data, password_data = get_sign_up_data()


        # Проверка, что имя не пустое
        assert name_data, "Поле «Имя» не может быть пустым"

        # Проверка корректности формата email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        assert re.match(email_pattern, email_data), "Email должен быть в формате: login@domain"

        # Проверка минимальной длины пароля
        assert len(password_data) >= 6, "Пароль должен содержать минимум 6 символов"

        # Заполняем форму регистрации
        name_field = driver.find_element(*Mestolocators.NAME_FIELD)
        name_field.send_keys(name_data)

        email_field = driver.find_element(*Mestolocators.EMAil_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*Mestolocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        submit_button = driver.find_element(*Mestolocators.SUBMIT_BUTTON)
        submit_button.click()

        # Ожидаем появления кнопки выхода (логина)
        logout_button = WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.visibility_of_element_located(Mestolocators.LOGOUT_BUTTON))
        assert logout_button.is_displayed(), "Кнопка выхода не доступна"
        assert logout_button.is_enabled(), "Кнопка выхода доступна"

    def test_signup_invalid_password(self, driver):
        # Переход на страницу регистрации
        driver.get(f'{Config.URL}/register')

        # Получаем данные для регистрации
        name_data, email_data, password_data = get_sign_up_data()

        # Заполняем форму регистрации с некорректным паролем (меньше 6 символов)
        name_field = driver.find_element(*Mestolocators.NAME_FIELD)
        name_field.send_keys(name_data)

        email_field = driver.find_element(*Mestolocators.EMAIL_FIELD)
        email_field.send_keys(email_data)

        password_field = driver.find_element(*Mestolocators.PASSWORD_FIELD)
        password_field.send_keys('123')  # Некорректный пароль (менее 6 символов)

        # Нажимаем на кнопку регистрации
        submit_button = driver.find_element(*Mestolocators.SUBMIT_BUTTON)
        submit_button.click()

        # Ожидаем появления сообщения об ошибке
        alert = WebDriverWait(driver, Config.TIMEOUT).until(EC.alert_is_present())

        # Проверяем, что появляется соответствующее сообщение об ошибке
        assert "Пароль должен содержать минимум 6 символов" in alert.text, "Ошибка не отображается"

        # Закрываем alert
        alert.accept()

    def test_signup_invalid_email(self, driver):
        # Переход на страницу регистрации
        driver.get(f'{Config.URL}/register')

        # Получаем данные для регистрации
        name_data, email_data, password_data = get_sign_up_data()

        # Заполняем форму регистрации с некорректным email (невалидный формат)
        name_field = driver.find_element(*Mestolocators.NAME_FIELD)
        name_field.send_keys(name_data)

        email_field = driver.find_element(*Mestolocators.EMAIL_FIELD)
        email_field.send_keys('invalid_email')  # Некорректный email

        password_field = driver.find_element(*Mestolocators.PASSWORD_FIELD)
        password_field.send_keys(password_data)

        # Нажимаем на кнопку регистрации
        submit_button = driver.find_element(*Mestolocators.SUBMIT_BUTTON)
        submit_button.click()

        # Ожидаем появления сообщения об ошибке
        alert = WebDriverWait(driver, Config.TIMEOUT).until(EC.alert_is_present())

        # Проверяем, что появляется соответствующее сообщение об ошибке
        assert "Email должен быть в формате" in alert.text, "Ошибка не отображается"

        # Закрываем alert
        alert.accept()

