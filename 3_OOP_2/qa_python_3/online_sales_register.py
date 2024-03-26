import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheaue(self, name):
        if 0 > len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for name in self.__name_items:
            total.append(self.__item_price[name])
        if self.__number_items > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 20:
                twenty_percent_tax.append(name)
                total.append(self.__item_price[name])
        if self.__number_items > 10:
            return sum(total) * 0.9 * 0.2
        else:
            return sum(total)*0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 10:
                ten_percent_tax.append(name)
                total.append(self.__item_price[name])
        if self.__number_items > 10:
            return sum(total) * 0.9 * 0.1
        else:
            return sum(total)*0.1

    def total_tax(self):
        result_tax = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return result_tax

    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) is not int:
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'
