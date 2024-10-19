import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline() != '':
            all_data.append(file.readline())









if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.now()
    for name in filenames:
        read_info(name)
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)
