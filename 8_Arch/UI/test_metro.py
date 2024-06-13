from selenium import webdriver
from metro_page import MetroPage


class TestMetroRoute:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_travel_time(self):
        self.driver.get('https://qa-metro.stand-1.praktikum-services.ru/')

        metro_page = MetroPage(self.driver)
        metro_page.wait_for_load_metro_map()
        metro_page.set_from_station('Красные Ворота')
        metro_page.set_to_station('Фрунзенская')

        assert metro_page.get_travel_time() == '≈ 13 мин.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
