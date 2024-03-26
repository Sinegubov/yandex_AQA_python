# создаём собственный класс-исключение и наследуем его от класса Exception
class MyCustomException(Exception):

    # задаём метод инициации, который на вход может принимать аргумент
    def __init__(self, message=None):
        self.message = message

    # задаём метод для вывода информации на экран
    def __str__(self):
        if self.message:
            return f'MyCustomException: {self.message}'
        return 'Произошло исключение MyCustomException'

def get_some_sum(some_arg):
    try:
        print(len(some_arg[0]) + 2)
    except Exception as e:
        # допиши код вызова исключения тут
        raise MyCustomException(f"Вызвано исключение из-за {type(e).__name__}!")

get_some_sum('это строка')
get_some_sum(['это', 'список'])
get_some_sum({'2': 1})

# должно быть выведено примерно следующее
# 3
# 5
# MyCustomException: MyCustomException: Вызвано исключение из-за KeyError!