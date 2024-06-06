# добавь нужные импорты для использования параметризации
import pytest

SUPPORTED_TIMEZONES = ['UTC', 'Europe/Moscow', 'Asia/Tokyo', 'America/New_York']

# напиши функцию is_timezone_supported для проверки поддерживаемых зон


def is_timezone_supported(timezone):
    return timezone in SUPPORTED_TIMEZONES
# добавь тест test_timezone_support с параметризацией для проверки этих зон:
# 'UTC', 'Europe/London', 'Asia/Tokyo', 'Pacific/Auckland'


@pytest.mark.parametrize("timezone, expected_result", [
    ('UTC', True),
    ('Europe/London', False),
    ('Asia/Tokyo', True),
    ('Pacific/Auckland', False)])
def test_timezone_support(timezone, expected_result):
    assert is_timezone_supported(timezone) == expected_result
