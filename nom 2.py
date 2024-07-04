tchislo1 = int(input())
tchislo2 = int(input())
tchislo3 = int(input())

if tchislo1 == tchislo3 == tchislo2:
    print('3 одинаковых числа')
elif tchislo1 == tchislo2 or tchislo2 == tchislo3 or tchislo1 == tchislo3:
    print('2 одинаковых числа')
else:
    print('Одинаковых чисел нет')