class OfficeWorker:
  def say(self):
    print("Harold: Я люблю работать.")


class RealCharacter:
  def express_feeling(self):
    print("Harold: Я скрываю боль.")


class HideThePainHarold(OfficeWorker, RealCharacter):
  pass


harold = HideThePainHarold()
harold.say()
harold.express_feeling()