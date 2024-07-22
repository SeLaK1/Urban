
def podschet_summ(*perem):
    global summ
    for i in perem:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            for key in i:
                if isinstance(key, int) and isinstance(i[key], int):
                    summ += key + i[key]
                elif isinstance(key, str) and isinstance(i[key], int):
                    summ += len(key) + i[key]
                elif isinstance(key, int) and isinstance(i[key], str):
                    summ += key + len(i[key])
                else:
                    summ += len(key) + len(i[key])
        else:
            podschet_summ(*i)

summ = 0
data_structure = [ [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}]) ]
podschet_summ(data_structure)
print(summ)
