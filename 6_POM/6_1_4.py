# импортировали класс для поиска локаторов By
from selenium.webdriver.common.by import By
from selenium import webdriver

# Шаг 1. Объявили класс страницы — page object


class LoginPageMesto:
    # Шаг 2. Описали локатор для заголовка «Вход»
    entrance_title = [By.CLASS_NAME, 'auth-form__title']
    # Описали локатор заголовка «Регистрация»
    registration_header = [By.CLASS_NAME, 'header__auth-link']

    # Шаг 3. Добавили конструктор класса
    def __init__(self, driver):
        self.driver = driver  # Инициализировали его атрибуты

    # Шаг 4. Добавили проверки
    # метод проверяет наличие надписи "Вход"
    def check_presence_of_entrance_title(self):
        actually_value = self.driver.find_element(*self.entrance_title).text
        expected_value = 'Вход'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод проверяет наличие надписи "Регистрация"
    def check_presence_of_header_registration(self):
        actually_value = self.driver.find_element(*self.registration_header).text
        expected_value = 'Регистрация'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'


login_page = LoginPageMesto(webdriver.Chrome())
