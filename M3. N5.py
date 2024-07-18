
def proizv_cifr(digit):
    str_digit = str(digit)
    first = int(str_digit[0])
    if len(str_digit) == 1:
        return digit
    else:
        return first * proizv_cifr(int(str_digit[1:]))

digit = int(input('Введите значение: '))
print(f'Результат числа {digit}: {proizv_cifr(digit)}')