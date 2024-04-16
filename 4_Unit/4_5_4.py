import pytest


def check_file_size(filename, file_size):
    # условие: имя файла оканчивается на '.pdf'
    if filename.endswith('.pdf'): # метод endswith() проверяет совпадение с последними символами строки
        return file_size < 5000   # размер не может превышать 5000 Кб

    # условие: имя файла оканчивается на '.txt'
    if filename.endswith('.txt'):
        return file_size < 1000  # размер не может быть больше 1000 Кб

    return False  # если файл больше лимита, возвращается False


@pytest.mark.parametrize(
    'filename,file_size',            # Параметры передали в декоратор в виде единой строки
    [
        ['great_gatsby.txt', 800],   # Тестовые данные передали вторым аргументом,
        ['crazy_python.pdf', 1500],  # они тут в виде списка списков
        ['memology.txt', 333]
    ]
)
def test_files(filename, file_size):  # Тестовой функции передали оба аргумента
    assert check_file_size(filename, file_size) # Тестируемая функция с ассертом