class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


# наследуй класс Predator от Species, реализуй конструктор и метод survive()
class Predator(Species):
    def __init__(self, population, growth_rate, hunting_success_rate):
        self.hunting_success_rate = hunting_success_rate
        super().__init__(population, growth_rate)

    def survive(self):
        self.population -= self.population*(1-self.hunting_success_rate)


predator = Predator(1000, 0.02, 1.05)
print(predator.population)
predator.survive()
print(predator.population)