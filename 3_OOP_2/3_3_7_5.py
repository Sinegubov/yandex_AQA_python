class MyAttributeException(Exception):

    # задаём метод инициации, который на вход может принимать аргумент
    def __init__(self, message=None):
        self.message = message

    # задаём метод для вывода информации на экран
    def __str__(self):
        if self.message:
            return f'MyAttributeException: {self.message}'
        return 'Произошло исключение MyAttributeException'


class Bird:

    def __init__(self, name):
        self.head = 1
        self.tail = 1
        self.paws = 2
        self.wings = 2
        self.name = name

    def get_info_about_bird(self):
        return f'У птицы по имени {self.name} {self.paws} лапы, {self.tail} хвост и {self.head} голова. А ещё {self.wings} крыла!'


# допиши код ниже
def get_info_about_animal(some_animal, attribute):
    try:
        if attribute == 'feathers':
            animal_attribute = some_animal.feathers
        else:
            animal_attribute = some_animal.name
    # допиши блок кода здесь
    except AttributeError:
        raise MyAttributeException('Неизвестное количество перьев у птицы')
    finally:
        print(some_animal.get_info_about_bird())

# должен получиться такой вывод:
# У птицы по имени Кеша 2 лапы, 1 хвост и 1 голова. А ещё 2 крыла!
# У птицы по имени Кеша 2 лапы, 1 хвост и 1 голова. А ещё 2 крыла!
# MyAttributeException: Неизвестное количество перьев у птицы

bird = Bird('Кеша')
get_info_about_animal(bird, 'wings')  # выведет информацию о животном
get_info_about_animal(bird, 'feathers')  # О количестве перьев ничего не известно и информацию о животном