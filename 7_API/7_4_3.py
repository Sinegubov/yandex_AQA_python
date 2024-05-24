from unittest.mock import Mock

def test_calculate():
    mock = Mock()
    mock.calculate.return_value = 505

    assert mock.calculate() == 505 # тест будет пройден