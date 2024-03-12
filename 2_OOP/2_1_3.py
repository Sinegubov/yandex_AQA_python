class ElectronicDevice:
    def __init__(self, standby_power):
        self.standby_power = standby_power

    def consume_power(self, hours):
        return self.standby_power * hours

class Laptop(ElectronicDevice):
    def __init__(self, standby_power, working_power):
        super().__init__(standby_power)  # вызов конструктора суперкласса
        self.working_power = working_power

    def consume_power(self, hours, working_hours):  # переопределение метода
        return self.standby_power * (hours - working_hours) + self.working_power * working_hours

class AirConditioner(ElectronicDevice):
    def __init__(self, standby_power, cooling_power):
        super().__init__(standby_power)  # вызов конструктора суперкласса
        self.cooling_power = cooling_power

    def consume_power(self, hours, cooling_hours):  # переопределение метода
        return self.standby_power * (hours - cooling_hours) + self.cooling_power * cooling_hours

laptop = Laptop(standby_power=10, working_power=100)
air_conditioner = AirConditioner(standby_power=5, cooling_power=150)

# расход энергии для ноутбука за 24 часа с 8 рабочими часами
print(laptop.consume_power(hours=24, working_hours=8))              # 960

# расход энергии для кондиционера за 24 часа с 12 часами охлаждения
print(air_conditioner.consume_power(hours=24, cooling_hours=12))    # 1860