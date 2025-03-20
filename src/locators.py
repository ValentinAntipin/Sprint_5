from selenium.webdriver.common.by import By


class Mestolocators:


    NAME_FIELD = By.XPATH, "//*(@class, 'text input__textfield text_type_main-default')"
    EMAIl_FIELD = By.XPATH, "//*[@id='mail']"
    PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"
    EMAIL_HEADER = By.XPATH, "//p[contacts(@class, 'user')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"
    LOGIN_BUTTON = By.XPATH,"//button['Войти в аккаунт']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ""
    LOGIN_BUTTON_IN_REGISTRATION = By.XPATH, ""
    LOGIN_BUTTON_IN_PASSWORD_RECOVERY = By.XPATH, ""
    CONSTRUCTOR_BUTTON = By.XPATH, ""
    LOGO = By.XPATH, ""
    BUNS_BUTTON = By.XPATH, ""
    SAUCES_BUTTON = By.XPATH, ""
    TOPPINGS_BUTTON = By.XPATH, ""