import pytest


class TestDataDictionary:
    data_dictionary = {}

    # добавь setup_class
    @classmethod
    def setup_class(cls):
        cls.data_dictionary = {"A": 1, "B": 2}

    def test_check_first_element(self):
        assert self.data_dictionary["A"] == 1

    def test_check_second_element(self):
        assert self.data_dictionary["B"] == 2

    @classmethod
    def teardown_class(cls):
        cls.data_dictionary.clear()