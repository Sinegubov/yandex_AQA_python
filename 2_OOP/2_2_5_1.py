# место для миксинов
class BatTransformableMixin:
    def transform_into_bat(self):
        return "Превращение в летучую мышь"

class WolfTransformableMixin:
    def transform_into_wolf(self):
        return "Превращение в волка"

class RunnableMixin:
    def run(self):
        return "Беги, Форрест, беги!"
# наследуется от RunnableMixin
class Human(RunnableMixin):
    pass


# наследуется от BatTransformableMixin и RunnableMixin
class Vampire(BatTransformableMixin, RunnableMixin):
    pass


# наследуется от WolfTransformableMixin
class Werewolf(WolfTransformableMixin):
    pass


human = Human()
vampire = Vampire()
werewolf = Werewolf()

print(human.run())
print(vampire.run())
print(vampire.transform_into_bat())
print(werewolf.transform_into_wolf())