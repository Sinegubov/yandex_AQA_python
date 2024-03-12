class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


class Predator(Species):
    def __init__(self, population, growth_rate, hunting_success_rate):
        # явный вызов класса Species
        Species.__init__(self, population, growth_rate)
        self.hunting_success_rate = hunting_success_rate

    def survive(self):
        self.population -= self.population * (1 - self.hunting_success_rate)


class Herbivore(Species):
    def __init__(self, population, growth_rate, food_availability):
        # явный вызов класса Species
        Species.__init__(self, population, growth_rate)
        self.food_availability = food_availability

    def grow(self):
        if self.food_availability > 0.2:
            self.population += self.growth_rate * self.population
            self.food_availability -= 0.15
        else:
            self.migrate()

    def migrate(self):
        self.population -= 0.2 * self.population
        self.food_availability = 0.3



# наследуйся от классов Predator и Herbivore, реализуй конструктор и
# переопредели метод grow()
class Omnivore(Predator, Herbivore):
    def __init__(self, population, growth_rate, hunting_success_rate, food_availability, diet_balance):
        Predator.__init__(self, population, growth_rate, hunting_success_rate)
        Herbivore.__init__(self, population, growth_rate, food_availability)
        self.diet_balance = diet_balance

    def grow(self):
        if self.diet_balance >= 0.5:
            Predator.survive(self)
        else:
            Herbivore.grow(self)


omnivore_herbivore = Omnivore(1000, 0.05, 1, 0.6, 0.4)
print(omnivore_herbivore.population)
omnivore_herbivore.grow()
print(omnivore_herbivore.population)

omnivore_predator = Omnivore(500, 0.02, 1.2, 0.5, 0.6)
print(omnivore_predator.population)
omnivore_predator.grow()
print(omnivore_predator.population)
