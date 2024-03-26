# создаём собственный класс-исключение
class MySuperException(Exception):

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        # если при вызове нашего исключения было передано сообщение
        if self.message:
            # добавляем его в строку, которую вернёт и выведет на экран
            # исключение при вызове
            return f'MySuperException: {self.message}'
        # если условие не выполнилось, то есть никакое сообщение при вызове
        # исключения не передавали, вернём какое-то дефолтное сообщение
        return 'Произошло исключение MySuperException'

def test_my_super_exception():
    try:
        raise MySuperException('Вызвано самое суперское исключение!')
    except MySuperException as e:
        print(e.with_traceback(None))


test_my_super_exception()  # MySuperException: Вызвано самое суперское исключение!