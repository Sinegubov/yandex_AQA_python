from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PageWeather:
 # опишем элементы на странице
    item = ['локатор']
    main_title = ['локатор']
    site_logo = ['локатор']
    settlement = ['локатор']

    def __init__(self, driver):
        self.driver = driver

    def check_settlement_name(self):
        actually_settlement = self.driver.find_element(*self.main_title).text
        expected_settlement = 'населённый пункт'
        assert actually_settlement == expected_settlement

    def select_settlement(self):
        self.driver.find_element(*self.item).click()

    def set_settlement(self):
        self.driver.find_element(*self.settlement).send_keys('населённый пункт')

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.site_logo))

class TestPageWeather:
    driver = None

    @classmethod
    def setup_class(cls):
        # создадим драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()
        # перейдём на страницу погоды
        cls.driver.get('url сайта')
        # создадим объект класса страницы погоды
        cls.home_page = PageWeather(cls.driver)

    def test_weather_for_selected_settlement(self):
        # дождёмся загрузки страницы
        self.home_page.wait_for_load_home_page()
        # введём название населённого пункта
        self.home_page.set_settlement()
        # выберем из списка предложенных названий нужный нам населённый пункт
        self.home_page.select_settlement()
        # проверим название населённого пункта, для которого выводится погода
        self.home_page.check_settlement_name()

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit()