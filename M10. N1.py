import time
from threading import Thread as thr
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    file.close()

start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end1 = datetime.now()
print(end1-start)

start1 = datetime.now()
thr_1 = thr(target=write_words, args=(10, 'example5.txt'))
thr_2 = thr(target=write_words, args=(30, 'example6.txt'))
thr_3 = thr(target=write_words, args=(200, 'example7.txt'))
thr_4 = thr(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
end2 = datetime.now()
print(end2-start1)
