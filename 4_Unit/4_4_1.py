class Dog:

    def __init__(self, name):  # констуктор класса, который в качестве аргумента принимает имя собачки
        self.name = name
        self.happiness = 50    # уровень счастья у новой собачки всегда 50

    def pet_the_dog(self):     # метод, который увеличивает уровень счастья собачки на 10%
        self.happiness += 10


class TestDog:

    def test_name_of_dog_true(self):
        dog = Dog('Sharik')  # создание нового экземпляра класса

        assert dog.name == 'Sharik'  # проверка корректности имени в созданном экземпляре

    def test_default_value_happiness_true(self):
        dog = Dog('Sharik')  # создание нового экземпляра класса

        assert dog.happiness == 50  # проверка корректности значения уровня счастья в созданном экземпляре

    def test_pet_the_dog_true(self):
        dog = Dog('Sharik')  # создание нового экземпляра класса
        dog.pet_the_dog()  # вызов метода, увеличивающего уровень счастья собачки на 10 процентов

        assert dog.happiness == 60  # проверка, что уровень счастья равен 60-ти процентам (50 + 10)
