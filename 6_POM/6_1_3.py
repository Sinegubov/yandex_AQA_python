# импортировали класс для поиска локаторов By
from selenium.webdriver.common.by import By

# Шаг 1. Объявили класс страницы — page object


class LoginPageMesto:
    # Шаг 2. Описали локатор поля «Email»
    email_field = [By.ID, 'email']
    # Описали локатор поля «Пароль»
    password_field = [By.ID, 'password']

    # Шаг 3. Добавили конструктор класса
    def __init__(self, driver):
        self.driver = driver  # Инициализировали его атрибуты

    # Шаг 4. Добавили действия с элементами как методы
    # метод заполняет поле «Email»
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    # метод заполняет поле «Пароль»
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    # Шаг 5. Добавили проверки
    # метод проверяет соответствие поля «Email» переданным данным
    def check_email_value(self, email):
        actually_value = self.driver.find_element(*self.email_field).get_property("value")
        expected_value = email
        assert actually_value == expected_value, \
            f'Ожидалось значение поля Email: "{expected_value}", получено "{actually_value}"'

    # метод проверяет соответствие поля «Пароль» переданным данным
    def check_password_value(self, password):
        actually_value = self.driver.find_element(*self.password_field).get_property("value")
        expected_value = password
        assert actually_value == expected_value, \
            f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'
