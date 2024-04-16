import pytest


def check_name(name):
    if name[0] == name[0].upper():  # условие: первая буква имени заглавная
        return True                 # upper() — это встроенный метод Python
    # он преобразует символы строки в символы верхнего регистра и возвращает их

    return False

@pytest.mark.parametrize("name", ['George', 'Anna', 'Matt'])
def test_check_user_name(name):
    assert check_name(name)