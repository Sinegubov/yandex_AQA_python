from unittest.mock import Mock, patch

class User:

    def __init__(self, database):
        self.database = database

    def get_user_details(self, user_id):
        return self.database.get_user_details(user_id)


class Database:

    def get_user_details(self, user_id):
        # эмулируем запрос к базе данных
        # в реальном приложении здесь будет логика запроса к БД
        if user_id == '1':
            return {'data': 'User data'}
        else:
            return {'data': 'User not found'}


class TestUser:
    @patch('user.Database')
    def test_get_current_user_details(self, mock_database):
        mock_database = Mock()
        mock_database.get_user_details.return_value = {'data': 'User data'}
        user = User(mock_database)
        assert {'data': 'User data'} == user.get_user_details('1')
