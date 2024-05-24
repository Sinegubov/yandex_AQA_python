from unittest.mock import Mock
# создали мок-объект с именем mock
mock = Mock()

class Order:

    def __init__(self):
        self.mockachino = None        # сколько пользователь заказал моккачино
        self.americano = None         # сколько — американо
        self.sugar = None             # нужно ли добавить сахар и молоко
        self.milk = None