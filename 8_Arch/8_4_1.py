import unittest
from unittest.mock import Mock


def should_open_windows(weather_data):
    if weather_data.get('rain') or weather_data.get('temperature') < 10:
        return False
    return True


class TestShouldOpenWindows(unittest.TestCase):
    def test_rainy_weather(self):
        # Мок данных погоды, когда ожидается дождь
        mock_weather_data = {'temperature': 15, 'rain': True}
        self.assertFalse(should_open_windows(mock_weather_data))

    def test_cold_weather(self):
        # Мок данных погоды, когда температура ниже 10 градусов
        mock_weather_data = {'temperature': 5, 'rain': False}
        self.assertFalse(should_open_windows(mock_weather_data))

    def test_ideal_conditions(self):
        # Мок данных погоды, когда условия идеальны для открытия окон
        mock_weather_data = {'temperature': 20, 'rain': False}
        self.assertTrue(should_open_windows(mock_weather_data))