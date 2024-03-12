class Animal:
    def __init__(self, energy):
        self.energy = energy

    def move(self, distance):
        self.energy -= distance * 0.1  # каждый метр движения требует 0.1 единицы энергии

        return self.energy

class Bird(Animal):
    def __init__(self, energy, wind):
        super().__init__(energy)
        self.wind = wind  # скорость ветра может влиять на энергию птицы во время движения

    def move(self, distance):
        self.energy = super().move(distance)  # начинаем движение так же, как и другие животные
        self.energy += self.wind * 0.05 * distance  # но затем восстанавливаем часть энергии, если есть ветер

        return self.energy