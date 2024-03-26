def multiplication(some_arg):
    try:
        print(int(some_arg[0]) * 2)
    except ValueError:
        print(len(some_arg))
    except KeyError:
        print(len(some_arg) * 2)
    except IndexError:
        print(len(some_arg) * 3)


multiplication('some_arg')  # 8
multiplication('234567')  # 4
multiplication([3, 2, 1])  # 6
multiplication({2: 1})  # 2
multiplication([])  # 0