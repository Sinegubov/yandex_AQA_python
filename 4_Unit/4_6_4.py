import pytest

class TestUsers:

    @pytest.fixture(autouse=True)
    def user(self):
     # self.user может быть сложным объектом с большим количеством параметров
        self.user = {'name': 'User', 'bank_account': 15161719}
        return self.user

    def test_user_bank_account(self):
        # выполняются действия с self.user, в процессе которых объект меняется
        # например, отправляем запрос на смену банковского счета для self.user
        ...
        self.user['bank_account'] = 218714
        ...
        assert self.user == {'name': 'User', 'bank_account': 218714}

    def test_user_name(self):
        # для этого теста self.user такой же, как был изначально
        assert self.user == {'name': 'User', 'bank_account': 15161719}