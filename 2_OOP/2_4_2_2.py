class MyAnimals:
    all_my_animals = 0

    def __init__(self):
        MyAnimals.all_my_animals = MyAnimals.all_my_animals + 1

    @classmethod
    def get_aminals_count(cls):
        return f'I have {cls.all_my_animals}!'


# Создаём объекты класса
my_cat = MyAnimals()
# при создании объекта вызвали метод init, он изменил значение переменной на 1
my_dog = MyAnimals()
# значение переменной стало 2
my_bird = MyAnimals()

# Вызываем classmethod
print(MyAnimals.get_aminals_count())  # 3