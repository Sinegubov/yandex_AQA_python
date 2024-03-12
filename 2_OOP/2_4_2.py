from datetime import date


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = date.today().year
        return cls(name, current_year - birth_year)


# создали объект класса с годом рождения вместо возраста
dog = Dog.from_birth_year('Рекс', 2015)  # вызываем метод класса
print(dog.age)  # 8