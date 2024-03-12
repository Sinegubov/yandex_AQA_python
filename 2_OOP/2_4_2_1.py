import random


class Cat:

    def __init__(self, name):
        self.name = name
        self.head = 1
        self.tail = 1
        self.paws = 4

    @classmethod
    def without_name(cls):
        sample_names = ['Барсик', 'Снежинка', 'Миса', 'Феликс']
        return cls(random.choice(sample_names))

cat = Cat.without_name()
print(cat.name)