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


h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))