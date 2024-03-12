class Dog:

    def __init__(self):
        self.head = 1
        self.paws = 4

    @staticmethod
    def get_a_portion_of_food(age):
        if age < 1:
            return 50
        elif 1 <= age < 7:
            return 100
        else:
            return 70