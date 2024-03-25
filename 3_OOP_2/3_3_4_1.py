def division(some_int):
    try: # попробуй выполнить действие ниже
        print(10 / some_int)
    except Exception as e: # если не получилось, поймай исключение и выполни действие далее
        print('division by zero')
        print(type(e).__name__)

division(0)
# будет напечатано:
# ZeroDivisionError
# division by zero