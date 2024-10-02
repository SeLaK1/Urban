# -*- coding: utf-8 -*-
import random
from threading import Thread, Lock
import time

class Bank:
    def __init__(self, balance=0, lock=Lock()):
        self.balance, self.lock = balance, lock

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand = random.randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос отклонен, недостатоно средств')

Depozit_Bank = Bank()

th1 = Thread(target=Bank.deposit, args=(Depozit_Bank,))
th2 = Thread(target=Bank.take, args=(Depozit_Bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {Depozit_Bank.balance}')


