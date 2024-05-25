from unittest.mock import patch


class OrderProcessor:
    def validate_order(self, order):       # метод ничего не возвращает
        pass                               # его реализация не важна для теста, поэтому
                                           # её заменяет pass
    def charge_payment(self, order, amount):
        pass

    def ship_order(self, order, address):
        pass

    def process_order(self, order, amount, address):
        self.validate_order(order)
        self.charge_payment(order, amount)
        self.ship_order(order, address)


order = "test_order"
amount = 100
address = "Улица 123"

@patch('order_processor.OrderProcessor.ship_order')  # замокали метод ship_order()
def test_process_order_ship_order(mock_ship_order):
    op = OrderProcessor()                            # создали объект класса
    op.process_order("test_order", 100, "Улица 123") # вызвали тестируемый метод

    mock_ship_order.assert_called_once()             # проверили, что метод вызвал
                                                     # mock_ship_order()

@patch('order_processor.OrderProcessor.charge_payment')  # замокали метод ship_order()
def test_process_order_charge_payment(mock_charge_payment):
    op = OrderProcessor()                            # создали объект класса
    op.process_order(order, amount, address)

    mock_charge_payment.assert_called_once_with()             # проверили, что метод вызвал
                                                     # mock_ship_order()
