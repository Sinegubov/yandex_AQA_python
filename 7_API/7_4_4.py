from unittest.mock import Mock      # импортировали класс, чтобы создать мок

# создали тестовый класс
class TestDelivery:

    def test_schedule_delivery(self):
        # создали мок-объект
        mock_details_provider = Mock()
        mock_details_provider.get_cost.return_value = 500  # указали возвращаемые значения для методов мока
        mock_details_provider.get_destination.return_value = 'Москва'

        # передали мок-объект в экземпляр класса Delivery
        delivery = Delivery(mock_details_provider)

        # запланировали доставку
        # метод использует значения, определённые в моке
        # проверяем результат метода: Доставка запланирована в город Москва. Стоимость: 500₽.
        assert delivery.schedule_delivery() == 'Доставка запланирована в город: Москва. Стоимость: 500 ₽.'
class Delivery:
    def __init__(self, details_provider):
        self.details_provider = details_provider

    def calculate_cost(self):              # рассчитывает стоимость доставки
        return self.details_provider.get_cost()

    def schedule_delivery(self):           # планирует доставку
        destination = self.details_provider.get_destination()
        cost = self.calculate_cost()
                return f"Доставка запланирована в город: {destination}. Стоимость: {cost} ₽."


class DetailsProvider:
    def __init__(self, name, cost, destination):
        self.name = name
        self.cost = cost
        self.destination = destination

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_destination(self):
        return self.destination