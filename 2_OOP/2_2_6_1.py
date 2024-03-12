# для класса Species реализуй конструктор и метод grow()
class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.growth_rate * self.population


species = Species(1000, 0.02)
print(species.population)
species.grow()
print(species.population)