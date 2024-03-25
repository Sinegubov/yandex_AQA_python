import datetime as dt

def get_some_sum(some_arg):
    start_time = dt.datetime.now()
    try:
        result = some_arg[0] + 2
    except TypeError:
        result = len(some_arg[0]) + 2
    except KeyError:
        result = 'Не удалось выполнить действие с элементом!'
    finally:
        stop_time = dt.datetime.now()
        print(f'Программа выполнилась за {stop_time - start_time}')
    return result

print(get_some_sum('это строка'))
print(get_some_sum(['это список']))
print(get_some_sum({'2': 1}))

# Получим примерно такой вывод
# Программа выполнилась за 0:00:00.000816
# 3
# Программа выполнилась за 0:00:00.000941
# 12
# Программа выполнилась за 0:00:00.001040
# Не удалось выполнить действие с элементом! 