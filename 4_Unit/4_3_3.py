def get_max_number_from_list(arg):  # объявление метода с соответствующим названием

    if type(arg) is not list:       # проверка на тип аргумента
        return 'Not list!'

    elif arg == []:                 # проверка, не пустой ли список
        return 'List is empty!'

    else:                          # если аргумент является непустым списком
        max_number = arg[0]        # объявление переменной наибольшего числа и присваивание ей в качестве значения по
        # умолчанию первого элемента списка
        for i in arg:              # перебор списка циклом
            if type(i) == int or type(i) == float:   # проверка, что тип элемента в списке - целое число или
                # вещественное
                if i > max_number:        # если элемент из списка больше установленного в переменной
                    max_number = i        # то присвоить новое наибольшее число как значение в переменную max_number
            else:
                return 'List contains a not number type element!'  # если проверка на корректный тип элемента
                # (целое или вещественное число) не пройдена, то вернуть соответствующее сообщение
        return max_number          # возвращение наибольшего числа из метода


def test_get_max_number_from_list_correct_list():
    arg = [0, 1, 2, 3, 4, -5, 6.5]
    assert get_max_number_from_list(arg) == 6.5


def test_get_max_number_from_list_not_list_error():
    arg = 'String'
    assert get_max_number_from_list(arg) == 'Not list!'


def test_get_max_number_from_list_empty_list_error():
    arg = []
    assert get_max_number_from_list(arg) == 'List is empty!'


def test_get_max_number_from_list_incorrect_type_element_error():
    arg = [0, 1, 2, 3, 4, -5, 6.5]
    assert get_max_number_from_list(arg) != 'List contains a not number type element!'
