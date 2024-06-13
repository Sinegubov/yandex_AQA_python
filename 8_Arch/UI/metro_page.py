from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MetroPage:
    metro_map = (By.CSS_SELECTOR, '.ymaps-2-1-79-map .ymaps-2-1-79-inner-panes')
    from_station_input = (By.CSS_SELECTOR, '.from-to-suggest__from-field input')
    to_station_input = (By.CSS_SELECTOR, '.from-to-suggest__to-field input')

    from_suggest_label = (By.XPATH, '//div[@style="display: block; top: 155.5px; left: 29px; width: 260px;"]//span[@class="station-label__text"]')
    to_suggest_label = (By.XPATH, '//div[@style="display: block; top: 200.5px; left: 29px; width: 260px;"]//span[@class="station-label__text"]')
    station_selected_icon = (By.CSS_SELECTOR, '.from-to-suggest__from-field [data-name="station-icon"] .station-label__icon')
    travel_time_label = (By.CSS_SELECTOR, '[data-block="route-list"] .route-list-item__time')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_metro_map(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.metro_map))

    def _set_station(self, station_name, station_input_selector):
        self.driver.find_element(*station_input_selector).send_keys(station_name)

    def _click_station_suggest(self, station_suggest_locator):
        station_suggest = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(station_suggest_locator)
        )
        station_suggest.click()

    def _wait_for_station_selected(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.station_selected_icon))

    def set_from_station(self, station_name):
        self._set_station(station_name, self.from_station_input)
        self._click_station_suggest(self.from_suggest_label)
        self._wait_for_station_selected()

    def set_to_station(self, station_name):
        self._set_station(station_name, self.to_station_input)
        self._click_station_suggest(self.to_suggest_label)
        self._wait_for_station_selected()

    def get_travel_time(self):
        travel_time_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.travel_time_label)
        )

        return travel_time_element.text
