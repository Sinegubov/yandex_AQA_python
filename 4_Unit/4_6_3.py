import pytest

# напиши фикстуру city_name
@pytest.fixture(scope="session")
def city_name():
    return []
# напиши фикстуру append_city
@pytest.fixture(scope="session")
def append_city(city_name):
    return city_name.append('Москва')

class TestClassCityName:
	  # напиши тест test_city_name_one_city_is_in_received_list
    def test_city_name_one_city_is_in_received_list(self, city_name, append_city):
        assert city_name == ['Москва']


class TestClassCityNameWithoutAppend:
	  # напиши тест test_city_name_one_city_is_in_received_list
        def test_city_name_one_city_is_in_received_list(self, city_name):
            assert city_name == ['Москва']