
def poisk_kratnih(tchislo):
    spisok_kratnih = []
    for i in range(2, tchislo+1):
        if tchislo % i == 0:
            spisok_kratnih.append(i)
            spisok_kratnih.append(tchislo//i)
    spisok_kratnih = set(spisok_kratnih)
    spisok_kratnih.discard(1)
    spisok_kratnih.discard(2)
    return sorted(spisok_kratnih)

def poisk_summ(spisok_kratnih):
    rezult = ''
    for i in range(1, max(spisok_kratnih)):
        for tchislo in spisok_kratnih:
            if i <= tchislo//2:
                if i != tchislo-i:
                    rezult += str(i) + str(tchislo-i)
    return rezult

perem = int(input('Введите значение: '))
print(poisk_summ(poisk_kratnih(perem)))
input() # для того, чтобы вставить проверку ниже ctrl+c/ctrl+v









