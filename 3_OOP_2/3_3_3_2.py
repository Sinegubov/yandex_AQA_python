def get_some_sum(some_arg):
    try:
        result = some_arg[0]
    except TypeError:
        result = 'Данный тип переменной не поддерживает получение элемента по индексу или ключу'
    except KeyError:
        result = 'Такого ключа нет в словаре'
    except Exception:
        result = 'Не удалось выполнить действие с элементом!'
    return result

print(get_some_sum('это строка')) # э
print(get_some_sum(['это', 'список'])) # это
print(get_some_sum({3: 'словарь'})) # Такого ключа нет в словаре
print(get_some_sum(3)) # Данный тип переменной не поддерживает получение элемента по индексу или ключу