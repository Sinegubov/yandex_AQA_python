from unittest.mock import Mock

def test_mockachino():
    mock_one = Mock()                      # создали мок-объект
    mock_one.mockachino = '1 чашка'        # присвоили атрибуту mockachino значение
    assert mock_one.mockachino == '1 чашка'


from unittest.mock import Mock

def test_sugar():
    mock_one = Mock()
    # с помощью метода добавили мок-объекту атрибут sugar
    mock_one.configure_mock(sugar='1 ложка')
    assert mock_one.sugar == '1 ложка' 