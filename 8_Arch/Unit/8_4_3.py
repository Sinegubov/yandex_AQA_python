# добавь импорты для параметризации
import pytest

# напиши функцию calculate_commission() для расчёта комиссии


def calculate_commission(transaction_type, amount):
    if transaction_type == "перевод":
        comission = max(0.01 * amount, 100)
    elif transaction_type == "покупка":
        comission = 0.02 * amount
    else:
        comission = 0.005 * amount
    return comission

# добавь тест test_calculate_commission и проверь следующие параметры:
# "перевод", 5000 | "перевод", 15000 | "покупка", 5000 | "вывод", 5000
@pytest.mark.parametrize("transaction_type, amount, expected_result", [
    ('перевод', 5000, 100),
    ('перевод', 15000, 150),
    ('покупка', 5000, 100),
    ('вывод', 5000, 25)])
def test_calculate_commission(transaction_type, amount, expected_result):
    assert calculate_commission(transaction_type, amount) == expected_result
