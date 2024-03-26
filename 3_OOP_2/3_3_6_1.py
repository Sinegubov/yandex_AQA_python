# создаём собственный класс-исключение и наследуем его от класса Exception
class MyCustomException(Exception):

    # задаём метод инициации, который на вход может принимать аргумент
    def __init__(self, message=None):
        self.message = message

    # задаём метод для вывода информации на экран
    def __str__(self):
        # если при вызове нашего исключения было передано сообщение
        if self.message:
            # добавляем его в строку, которую вернёт и выведет на экран
            # исключение при вызове
            return f'MyCustomException: {self.message}'
        # если условие не выполнилось, то есть никакое сообщение при вызове
        # исключения не передавали, вернём какое-то дефолтное сообщение
        return 'Произошло исключение MyCustomException'

def test_my_custom_exception():
    try:
        raise MyCustomException('Вызвано пользовательское исключение!')
    except MyCustomException as e:
        print(e)
        print(e.message) # имеем доступ к полям, как и в обычном классе!

test_my_custom_exception() # MyCustomException: Вызвано новое исключение!