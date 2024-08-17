from math import pi, sqrt
class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color, *__sides):
        self.__color, self.__sides = __color, __sides
        self.proverka()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *spisok_storon):
        check = True
        if len(spisok_storon) == len(self.__sides):
            for storona in spisok_storon:
                if not isinstance(storona, int) or storona <= 0:
                    check = False
        else:
            check = False
        return check

    def get_sides(self):
        return self.__sides

    def __len__(self):
        Perimetr = 0
        for storona in self.__sides:
            Perimetr += storona
        return Perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            if len(new_sides) == 1:
                self.__sides = new_sides[0]
            else:
                self.__sides = new_sides
            self.proverka()


    def proverka(self):
        list_= []
        if isinstance(self.__sides, tuple) and len(self.__sides) == 1:
            a = self.__sides[0]
            self.__sides = a
        if isinstance(self.__sides, int):
            a = self.__sides
            for i in range(self.sides_count):
                list_.append(self.__sides)
            self.__sides = list_
        elif (isinstance(self.__sides, list) or isinstance(self.__sides, tuple)) and len(self.__sides) != self.sides_count:
            for i in range(self.sides_count):
                list_.append(1)
            self.__sides = list_

class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self._Figure__sides/(2*pi)

    def get_square(self):
        return pi*(self.__radius()**2)
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = len(self) / 2
        rezult = p
        for x in self._Figure__sides:
            rezult *= p-x
        return sqrt(rezult)

class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self._Figure__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())