from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Класс страницы авторизации
class LoginPageMesto:
    email_field = [By.ID, 'email']
    password_field = [By.ID, 'password']
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()


# Класс заголовка
class HeaderPageMesto:
    # создай локатор для элемента c email в заголовке страницы
    header_user = [By.CLASS_NAME, 'header__user']

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы
    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_user))

    # метод для получения текста элемента в заголовке
    def email_in_header(self):
        return self.driver.find_element(*self.header_user).text


# класс с автотестом
class TestPraktikum:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_check_email_in_header(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-mesto.praktikum-services.ru/')

        # создай объект класса страницы авторизации
        login_page = LoginPageMesto(self.driver)
        # выполни авторизацию
        email = "sinegubov_8@gmail.com"
        password = "123"
        # передавай эти переменные внутрь метода
        login_page.login(email, password)

        # создай объект класса заголовка приложения
        header_page = HeaderPageMesto(self.driver)
        # дождись загрузки заголовка
        header_page.wait_for_load_header()
        # получи текст элемента в заголовке
        email_from_header = header_page.email_in_header()

        # сделай проверку, что полученное значение совпадает c email
        assert email_from_header == email

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()
