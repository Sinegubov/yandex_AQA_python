from selenium.webdriver.common.by import By

class LoginPageMesto:
    # локатор поля «Email»
    email_field = [By.ID, 'email']
    # локатор поля «Пароль»
    password_field = [By.ID, 'password']
    # локатор кнопки входа в приложение
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    # метод заполняет поле «Email»
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    # метод заполняет поле «Пароль»
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    # метод кликает по кнопке «Войти»
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # метод авторизации в приложении: объединяет ввод email, пароля и клик по кнопке
    # это и есть шаг
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()