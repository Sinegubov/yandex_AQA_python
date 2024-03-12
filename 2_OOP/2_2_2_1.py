class Animal:
  def __init__(self):
    self.distance_travelled = 0
    self.calories_consumed = 0

  def move(self):
    self.distance_travelled += 5

  def eat(self):
    self.calories_consumed += 10


class Plant:
  def __init__(self):
    self.height = 0
    self.energy_stored = 0

  def grow(self):
    self.height += 1

  def photosynthesize(self):
    self.energy_stored += 10


class ZombieHerbivore(Animal, Plant):
  def __init__(self):
    Animal.__init__(self)
    Plant.__init__(self)


zombie = ZombieHerbivore()
zombie.grow()  # height теперь будет 1
zombie.move()  # AttributeError: 'ZombieHerbivore' object has no attribute 'distance_travelled'
print(zombie.height)  # 1
print(zombie.distance_travelled)  # 5