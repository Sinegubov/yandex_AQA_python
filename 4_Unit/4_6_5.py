import pytest


class TestWeather:
    @pytest.fixture(autouse=True)
    def weather(self):
        self.weather = 'Температура воздуха составляет 25 градусов тепла'
        return self.weather

    def test_weather_return_text(self):
        assert self.weather == 'Температура воздуха составляет 25 градусов тепла'

    def test_weather_change_return_new_text(self):
        weather = self.weather.replace('25', '10')
        assert weather == 'Температура воздуха составляет 10 градусов тепла'
