from selenium.webdriver.common.by import By


class LoginPageMesto:
    # локатор поля «Email»
    email_field = [By.ID, 'email']
    # локатор поля «Пароль»
    password_field = [By.ID, 'password']
    # локатор кнопки входа в приложение
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']
    # добавь здесь локатор для кнопки «Регистрация»
    registration_button = [By.CLASS_NAME, "header__auth-link"]

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод проверяет, активна ли кнопка «Войти»
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.sign_in_button).is_enabled()

    # метод кликает по кнопке «Войти»
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # метод кликает по кнопке «Регистрация»
    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    # метод проверяет текст кнопки «Регистрация»
    def check_text_registration_button(self):
        registration_button_text = self.driver.find_element(*self.registration_button).text
        assert registration_button_text == 'Регистрация', 'Текст кнопки не равен Регистрация'
