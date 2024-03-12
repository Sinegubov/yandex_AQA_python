class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}.")


class SpiderMan(Person):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self, with_identity=False):
        super().introduce()
        if with_identity:
            print(f"Но вы можете знать меня как Человека-паука.")
            # переопредели метод суперкласса, используя super()
            # добавь новое условие, используя with_identity


peter = SpiderMan("Питер Паркер")
peter.introduce(with_identity=True)
# Привет, меня зовут Питер Паркер.
# Но вы можете знать меня как Человека-паука.
