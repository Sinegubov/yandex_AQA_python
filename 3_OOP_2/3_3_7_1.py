def subtraction(first_arg, second_arg):
    try:
        return second_arg - first_arg
    except Exception:
        return 'Операцию вычитания выполнить нельзя!'

print(subtraction(1, 2)) # 1
print(subtraction('строка', 2)) # Операцию вычитания выполнить нельзя!
print(subtraction([1, 2], 2)) # Операцию вычитания выполнить нельзя!