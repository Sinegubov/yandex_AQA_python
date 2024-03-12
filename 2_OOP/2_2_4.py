class Animal:
  def sound(self):
    return "тихое молчание"


class Dog(Animal):
  def sound(self):
    return "Гав!"


class Cat(Animal):
  def sound(self):
    return "Мяу!"


class CatDog(Dog, Cat):
  def sound(self):
    return Cat.sound(self) + ' ' + Dog.sound(self)


my_pet = CatDog()
print(my_pet.sound())
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Animal, Dog, Cat