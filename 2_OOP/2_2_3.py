class LandAnimal:
  def __init__(self):
    print("Вызвали init из LandAnimal")
    self.can_walk = True

  def walk(self):
    if self.can_walk:
      print("Ходит")
    else:
      print("Не может ходить")


class WaterAnimal:
  def __init__(self):
    print("Вызвали init из WaterAnimal")
    self.can_swim = True

  def swim(self):
    if self.can_swim:
      print("Плавает")
    else:
      print("Не может плавать")


class Amphibian(LandAnimal, WaterAnimal):
  def __init__(self):
    print("Вызвали init из Amphibian")
    super().__init__()  # вызовет LandAnimal.__init__(), но не WaterAnimal.__init__()


frog = Amphibian()
# Вызвали init из Amphibian
# Вызвали init из LandAnimal

print(frog.can_walk)  # True

# # Вызовет ошибку — AttributeError: 'Amphibian' object has no attribute 'can_swim',
# потому что WaterAnimal.__init__() не был вызван
print(frog.can_swim)