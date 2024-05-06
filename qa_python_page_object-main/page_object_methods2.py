from selenium.webdriver.common.by import By


class RegistrationPageMesto:
    # локатор поля «Email»
    email_field = ...
    # локатор поля «Пароль»
    password_field = ...
    # локатор кнопки "Зарегистрироваться"
    registration_button = ...

    # конструктор класса
    def __init__(self, driver):
        ...

    # метод заполняет поле «Email»
    def set_email(self, email):
        ...

    # метод заполняет поля «Пароль»
    def set_password(self, password):
        ...

    # метод кликает по кнопке «Зарегистрироваться»
    def click_registration_button(self):
        ...

    # метод регистрации в приложении: объединяет ввод email-а, пароля и клик по кнопке «Зарегистрироваться»
    def register(self, ...):
        ...