class Cat:

    def __init__(self, name):
        self.paws = 4
        self.tail = 1
        self.head = 1
        self.name = name

    def get_info_about_cat(self):
        return f'У кота {self.name} {self.paws} лапы, {self.tail} хвост и {self.head} голова'

def get_info_about_animal(some_animal, attribute):
    # пробуем получить информацию, которая находится в определённом поле
    try:
        # ветвим код в зависимости от названия атрибута
        if attribute == 'character':
            animal_attribute = some_animal.character
        else:
            animal_attribute = some_animal.paws
    # Обрабатываем исключение
    except AttributeError:
        print('О характере животного ничего не известно')
    # допиши блок кода тут
    else:
        print(cat.get_info_about_cat())

cat = Cat('Барсик')
get_info_about_animal(cat, 'paws') # выведет информацию о животном
get_info_about_animal(cat, 'character') # О характере животного ничего не известно