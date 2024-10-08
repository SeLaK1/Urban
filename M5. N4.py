def error_type1():
    raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
def error_type2():
    raise TypeError('При добавлении новых этажей, их количество должно быть целочисленным (type int)')
class house:
    house_history = []

    def __new__(сls, *args, **kwargs):
        сls.house_history.append(args[0])
        return object.__new__(сls)

    def __init__(self, name, count_of_floors):
        self.name = name
        self.count_of_floors = count_of_floors

    def go_to(self, new_floor):
        if new_floor > self.count_of_floors or new_floor < 1:
            print(f'{new_floor} этажа не существует, дом {self.count_of_floors} этажный')
        else:
            print(f'Поднимаемся в {self.name}:', *range(1, new_floor + 1))

    def __len__(self):
        return self.count_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.count_of_floors}'

    def __eq__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors == other_self.count_of_floors

    def __ne__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors != other_self.count_of_floors

    def __lt__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors < other_self.count_of_floors

    def __le__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors <= other_self.count_of_floors

    def __gt__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors > other_self.count_of_floors

    def __ge__(self, other_self):
        if not isinstance(other_self, house):
            error_type1()
        return self.count_of_floors >= other_self.count_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            error_type2()
        self.count_of_floors += value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            error_type2()
        self.count_of_floors += value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            error_type2()
        self.count_of_floors += value
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории и наших сердцах')

h1 = house('ЖК Эльбрус', 10)
print(house.house_history)
h2 = house('ЖК Акация', 20)
print(house.house_history)
h3 = house('ЖК Матрёшки', 20)
print(house.house_history)

del h2
del h3

print(house.house_history)
