class Student:
    def __init__(self, age=0, grade=0):
        self.__age = age
        self.__grade = grade

    @property                 # геттер для свойства age
    def age(self):
        return self.__age

    @age.setter               # cеттер для свойства age
    def age(self, value):
        if 0 <= value <= 100:
            self.__age = value
        else:
            self.__age = 0

    @property                 # геттер для свойства grade
    def grade(self):
        return self.__grade

    @grade.setter             # сеттер для свойства grade
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            self.__grade = 0

# создали объект
student = Student()
student.age = 20       # работает сеттер age
student.grade = 90     # работает сеттер grade

print(student.age)    # работает геттер age
# Выведет: 20

print(student.grade)  # работает геттер grade
# Выведет: 90 