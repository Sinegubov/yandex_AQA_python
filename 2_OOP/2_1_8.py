# создай классы Animal, Dog и Cat, в каждом из которых будет метод make_sound
class Animal:

    def __init__(self, energy):
        self.energy = energy

    def make_sound(self):
        self.energy -= 5
        return self.energy

class Dog(Animal):

    def make_sound(self):
        print(f"Гав")
        self.energy -= 10
        return self.energy


class Cat(Animal):

    def make_sound(self):
        print(f"Мяу")
        self.energy -= 2
        return self.energy
# пример использования
animal = Animal(100)
print(animal.make_sound())  # вывод: 95

dog = Dog(100)
print(dog.make_sound())  # вывод: "Гав" 90

cat = Cat(100)
print(cat.make_sound())  # вывод: "Мяу" 98