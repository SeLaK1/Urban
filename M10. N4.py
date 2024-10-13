# -*- coding: utf-8 -*-
import random
import time
from threading import Thread
import queue

class Table:
    def __init__(self, num, guest = None):
        self.number, self.guest = num+1, guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    que = queue.Queue()

    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            if not guest.is_alive():
                if True in [True if table.guest == None else False for table in self.tables]:
                    for table in self.tables:
                        if table.guest == None and not guest.is_alive():
                            table.guest = guest.name
                            guest.start()
                            print(f'{guest.name} сел за стол под номером {table.number}')
                            time.sleep(0.5)
                else:
                    self.que.put(guest)
                    print(f'{guest.name} в ожидании')
                    time.sleep(0.5)
        return guests

    def discuss_guests(self, *guests):
        while not self.que.empty() or False in [True if table.guest == None else False for table in self.tables]:
            for table in self.tables:
                SpisokOfLud = [[True, guest] if table.guest == guest.name and not guest.is_alive() else [False, guest] for guest in guests]
                for i in range(len(SpisokOfLud)):
                    if True == SpisokOfLud[i][0]:
                        table.guest = None
                        SpisokOfLud[i][1].join()
                        print(f'{SpisokOfLud[i][1].name} поел(ла) и ушёл(ла), cтол под номером {table.number} освободился')
                        break
                if table.guest == None and not self.que.empty():
                    guest = self.que.get()
                    table.guest = guest.name
                    guest.start()
                    print(f'-----Гость {guest.name} вышел из очереди и сел за стол под номером {table.number}')
        print('Кафе пустует!')


table_count = 5
# Создание столов
tables = [Table(number) for number in range(table_count)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]
print(guests)

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests(*guests)
