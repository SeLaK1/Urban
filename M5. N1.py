
class house:
    def __init__(self, name, count_of_floors):
        self.name = name
        self.count_of_floors = count_of_floors
    def go_to(self, new_floor):
        if new_floor > self.count_of_floors or new_floor < 1:
            print(f'{new_floor} этажа не существует, дом {self.count_of_floors} этажный')
        else:
            print(f'Поднимаемся в {self.name}:', *range(1, new_floor+1))

house1 = house('ЖК Горский', 18)
house2 = house('Домик в деревне', 2)

house1.go_to(8)
house2.go_to(10)

