class house:
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
            raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
        return self.count_of_floors == other_self.count_of_floors

    def __lt__(self, other_self):
        if not isinstance(other_self, house):
            raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
        return self.count_of_floors < other_self.count_of_floors

    def __le__(self, other_self):
        if not isinstance(other_self, house):
            raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
        return self.count_of_floors <= other_self.count_of_floors

    def __gt__(self, other_self):
        if not isinstance(other_self, house):
            raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
        return self.count_of_floors > other_self.count_of_floors

    def __ge__(self, other_self):
        if not isinstance(other_self, house):
            raise TypeError('При сравнении количесва этажей, все переменные должны быть домами (type house)')
        return self.count_of_floors >= other_self.count_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError('При добавлении новых этажей, их количество должно быть целочисленным (type int)')
        self.count_of_floors += value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            raise TypeError('При добавлении новых этажей, их количество должно быть целочисленным (type int)')
        self.count_of_floors += value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise TypeError('При добавлении новых этажей, их количество должно быть целочисленным (type int)')
        self.count_of_floors += value
        return self

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__