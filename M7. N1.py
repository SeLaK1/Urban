
class Shop:
    __filename = 'products.txt'

    def __init__(self):
        self.sklad = []
        file = open(self.__filename, 'r')
        for line in file:
            pozicia = ''
            for simvol in line:
                if simvol == ',':
                    break
                pozicia += simvol
            self.sklad.append(pozicia)
        file.close()
    def get_products(self):
        with open(self.__filename, 'r') as file:
            print(file.read())
            file.close()

    def add(self, *products):
        file = open(self.__filename, 'a')
        for items in products:
            if items.name in self.sklad:
                print(f'Продукт {items.name} уже есть в магазине')
            else:
                file.write(f'{items.name}, {items.weight}, {items.category}\n')
        file.close()

class Product:

    def __init__(self, name, weight, category):
        self.name, self.weight, self.category = name, weight, category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
s1.get_products()