def multiplication(some_arg):
    try:
        print(int(some_arg[0]) * 2)
    except Exception as e:
        if type(e) == ValueError:
            print(f"invalid literal for int() with base 10: '{some_arg[0]}'")
            print(f'{type(e).__name__}')
        elif type(e) == IndexError:
            print('list index out of range')
            print(f'{type(e).__name__}')
        elif type(e) == KeyError:
            print(0)
            print(f'{type(e).__name__}')

multiplication('some_arg')
multiplication('123456')
multiplication([1, 2, 3])
multiplication({2: 1})
multiplication([])

# результат выполнения должен быть таким:
# invalid literal for int() with base 10: 's'
# ValueError
# 2
# 2
# 0
# KeyError
# list index out of range
# IndexError