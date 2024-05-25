import requests

class User:

    def __init__(self, data):
        self.user = data

    def get_user_details(self, user_id):
        response = requests.get('http://some-account-uri/' + user_id)
        return {'status': response.status_code, 'data': response.text}

    from unittest.mock import Mock, patch  # (1)

    from user import User

    class TestUser:

        @patch('user.requests')  # (2)
        def test_get_current_user_details(self, mock_requests):  # (3)
            mock_response = Mock()  # (4)
            mock_response.status_code = 200
            mock_response.text = 'User data'
            mock_requests.get.return_value = mock_response  # (5)
            user = User(mock_response)  # (6)
            assert {'status': 200, 'data': 'User data'} == user.get_user_details('1')  # (7)