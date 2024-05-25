import time

# чтобы ничего не отвлекало,
# в классе реализованы только два метода
class User:

    ...  # другие атрибуты и методы класса
    ...
    ...

    def upload_photo(self, photo):
        ... # тут код, который загружает аватарку
        ...
        time.sleep(30)  # имитируем медленную работу метода
        return 'OK'

        def create_user_profile(self, photo_path):   # создаём профиль пользователя
        result = self.upload_photo(photo_path)
        if result == 'OK':
            return 'Профиль создан'
        else:
            return 'Не удалось создать профиль'



# создали тестовый класс
import pytest
from unittest.mock import patch    # (1)
from user import User

class TestUser:

    @patch('user.User.upload_photo')    # в декораторе — только путь к методу
    @pytest.mark.parametrize('value', ['OK', 'ERROR'])
    def test_create_user_profile(self, mock_upload_photo, value):
        mock_upload_photo.return_value = value
        user = User()
        assert user.create_user_profile('photo.png') == 'Профиль создан'