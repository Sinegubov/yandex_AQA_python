class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


# наследуй класс Herbivore от Species, реализуй конструктор и
# переопредели метод grow()
class Herbivore(Species):
    def __init__(self, population, growth_rate, food_availability):
        self.food_availability = food_availability
        super().__init__(population, growth_rate)

    def grow(self):
        if self.food_availability > 0.2:
            self.population += self.population * self.growth_rate
            self.food_availability -= 0.15
        elif self.food_availability <= 0.2:
            Herbivore.migrate(self)

    def migrate(self):
        self.population -= 0.2 * self.population
        self.food_availability = 0.3


herbivore = Herbivore(2000, 0.04, 0.3)
herbivore.grow()
print(herbivore.population)
print(herbivore.food_availability)
herbivore.grow()
print(herbivore.population)
print(herbivore.food_availability)
