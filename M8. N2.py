
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(len(numbers)):
         try:
            result += numbers[i]
         except TypeError:
             print(f'Некоректный тип данных для пдсчета суммы: {numbers[i]}')
             incorrect_data += 1
    return [incorrect_data, result]

def calculate_average(numbers):
    sr_znach = 0
    try:
        _list = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        sr_znach = _list[1]/(len(numbers)-_list[0])
        return sr_znach
    except ZeroDivisionError as exc:
        print(f'Ошибка вида {exc}')
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать