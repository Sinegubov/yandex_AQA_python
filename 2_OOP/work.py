class Medication:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def consume(self):
        print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


class Tablet(Medication):
    # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
    # добавь новый атрибут colour
    def __init__(self, name, dosage, colour):
        self.colour = colour
        super().__init__(name, dosage)

    def print_colour(self):
        print(f"Цвет таблетки - {self.colour}")


class Injection(Medication):
    # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
    # добавь новый атрибут needle_length
    def __init__(self, name, dosage, needle_length):
        self.needle_length = needle_length
        super().__init__(name, dosage)

    def consume(self):
        print(f"Инъекция {self.name} сделана. Доза - {self.dosage}")

    def print_needle_length(self):
        print(f"Длина иглы - {self.needle_length}")


tablet = Tablet("Наследин", 2, "Белый")
tablet.consume()       # Принято лекарство - Наследин. Доза - 2
tablet.print_colour()  # Цвет таблетки - Белый
injection = Injection('ООПин', 1, "Средняя")
injection.consume()     # Инъекция ООПин сделана. Доза - 1
injection.print_needle_length()  # Длина иглы - Средняя
