# импорт драйвера
from selenium import webdriver
# импорт класса страницы авторизации
from page_object import LoginPageMesto

class TestPraktikum:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('https://qa-mesto.praktikum-services.ru/')

        # создать объект класса страницы авторизации
        login_page = LoginPageMesto(self.driver)
        # выполнить авторизацию
        login_page.login('email учётной записи', 'пароль учётной записи')
        # проверить наличие кнопки «Выйти»
        login_page.check_presence_of_exit_button()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()