class Warrior:
  def __init__(self):
    self.strength = 10
    self.health = 100

  def attack(self):
    attack_power = self.strength * 5
    print(f"Атакуем с силой {attack_power}!")


class Mage:
  def __init__(self):
    self.magic = 10
    self.intelligence = 10

  def cast_spell(self):
    spell_power = self.magic * self.intelligence
    print(f"Применяем заклинание силой {spell_power}!")


# реализуй класс BattleMage с множественным наследованием
class BattleMage(Warrior, Mage):
  def __init__(self):
    Warrior.__init__(self)
    Mage.__init__(self)


battleMage = BattleMage()
battleMage.attack()
battleMage.cast_spell()