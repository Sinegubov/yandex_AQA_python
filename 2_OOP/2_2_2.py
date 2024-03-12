class LandAnimal:
  def __init__(self):
    self.can_walk = True

  def walk(self):
    if self.can_walk:
      print("Ходит")
    else:
      print("Не может ходить")


class WaterAnimal:
  def __init__(self):
    self.can_swim = True

  def swim(self):
    if self.can_swim:
      print("Плавает")
    else:
      print("Не может плавать")


class Amphibian(LandAnimal, WaterAnimal):
  def __init__(self):
    LandAnimal.__init__(self)  # вызвали конструктор первого суперкласса
    WaterAnimal.__init__(self)  # вызвали конструктор второго суперкласса


frog = Amphibian()
frog.walk()  # Ходит
frog.swim()  # Плавает