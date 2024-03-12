def digit_root(num):
    if not isinstance(num, int) or num > 10000000:
        return False
    elif num < 10:
        return num
    else:
        digital_sum = 0
        while num > 0:
            digital_sum += num % 10
            num //= 10
        if digital_sum >= 10:
            return digit_root(digital_sum)
        else:
            return digital_sum


print(digit_root(889987))
