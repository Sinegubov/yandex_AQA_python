from unittest.mock import Mock


class User:
    def __init__(self, user_data):
        self.user = user_data

    def get_user(self, user_id):
        return self.user.get(user_id)


class TestUser:
    def test_get_data_by_id(self):
        mock_data = Mock()
        user_data = {"id": "1", "name": "test"}
        mock_data.get.return_value = user_data

        user = User(mock_data)
        assert user.get_user("1") == user_data
