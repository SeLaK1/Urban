import requests
# По сути, данная библиотека позволяет отправлять HTTP-запросы веб-сервисам и получать от них соответствующие запрашиваемые данные.
# Она ускоряет и упрощает работу с запросами

if __name__ == '__main__':
    r = requests.get('https://en.wikipedia.org/wiki/Dill', auth=('user', 'pass'))
    print(r.status_code) # запрашиваем статус соединения ссайтом(по адресу выше)
    print(r.headers['content-type'])  # обращаемся к заголовку и запрашиваем тип контента
    res = requests.get('https://en.wikipredia.org/wiki/Dill')  # Создаём переменную, в которую сохраним код состояния запрашиваемой страницы.
    print(res)  # Выводим код состояния.

    # Session() - класс позволяющий создавать базовые запросы с сохранёнными параметрами, без повторного указания параметров, а так же
    # если мы отправляем несколько запросов на один и тот же хост, то соединение которое мы только что использовали будет использоваться повторно
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/sessioncookie/123489')
    r = s.get('https://httpbin.org/cookies')
    print(r.text)

print('-----------------------------------------------')
import numpy as np
# NumPy достаточно полезная библиотека, связанная с работой с многомерными массивами, матрицами и т.д. Помогает сократить потребление памяти при хранении данных
# Но данные в массиве должны быть одного типа.

if __name__ == '__main__':
    mas = np.array([[[1, 2, 3], [1, 2, 3]], [[2, 2, 2], [2, 2, 2]]]) # создание трехмерного массива или же матрицы 2*2
    print(mas[1, 1]) # пример образения к определенному элементу в массиве

    print(mas.shape) # возвращает количество элементов в каждм измерении (len(mas.shape) вернет количество измерений, как и функция mas.ndim)
    print(mas.dtype) # возвращает тип данных в массиве

    mas = np.linspace(0, 11, num=12) # создает массив автоматически заполненный элементами от a до b  с указанным шагом
    print(mas)
    print(np.hsplit(mas, 4)) # разделяет массив на n массивов по ровну

    mas = np.array([[1, 2, 9], [9, 5, 3], [4, 9, 6]])
    print(mas.max(axis=1)) # создает массив из максимальных элементов в строке

print('-----------------------------------------------')
import matplotlib.pyplot, matplotlib.pylab as plt
# Данная библиотека предназначена дляя визуализации данных в двумерной и трехмерной графике
# Способна создавать графики любых видов
import random

if __name__ == '__main__':
    plt.title('Современное искусство for URBAN')
    for _ in range(100):
        plt.scatter([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)], [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)],
                    color=['red', 'pink', 'yellow', 'blue'], linewidths=random.randint(1, 12))
    plt.xlabel('_____________________9000$_______________________')
    plt.ylabel('________________________________________________________________')
    plt.bar(0, 0, label='')
    plt.show()

