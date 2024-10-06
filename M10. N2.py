# -*- coding: utf-8 -*-
from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power, count_enemy=150):
        super().__init__()
        self.name, self.power, self.count_enemy = name, power, count_enemy

    def run(self):
        count_day = 0
        print(f'{self.name}, на нас напали враги!')
        while self.count_enemy-self.power > 0:
            time.sleep(1)
            count_day += 1
            self.count_enemy -= self.power
            print(f'{self.name} сражается уже {count_day} днень(дня), осталось {self.count_enemy} врагов')
        print(f'{self.name} одержал победу за {count_day+1} дней(дня)')

first_knight = Knight('----Sir Lancelot', 10)   
second_knight = Knight('Sir Galahad', 20)
knight = []

knight.append(first_knight)
knight.append(second_knight)

for sluga in knight:
    sluga.start()

for sluga in knight:
    sluga.join()

print('Все битвы завешены')

