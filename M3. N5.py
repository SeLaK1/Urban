
def proizv_cifr(digit):
    if len(str(digit)) == 1:
        if digit == 0:
            return 1
        else:
            return digit
    else:
        return int(str(digit)[0]) * proizv_cifr(int(str(digit)[1:]))

digit = int(input('Введите значение: '))
print(f'Результат числа {digit}: {proizv_cifr(digit)}')
