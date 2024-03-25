# функция принимает на вход аргумент любого типа
def get_size(some_arg):
    try:
        print(10 / len(some_arg[0]))
    # допиши код перехвата ошибок и их обработки здесь
    except (IndexError, KeyError) as e:
        print(f'Произошла ошибка {type(e).__name__}. Узнать размер нельзя!')

get_size('это строка') # 1
get_size(['это', 'список']) # 3
get_size({'это': 'словарь'}) # Произошла ошибка KeyError. Узнать размер нельзя!
get_size('') # Произошла ошибка IndexError. Узнать размер нельзя!