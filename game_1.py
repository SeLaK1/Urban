def win_or_no(pole):
    if ((pole[0][0] == pole[1][1] == pole[2][2]) and pole[0][0] != '*') or ((pole[1][0] == pole[1][1] == pole[1][2]) and pole[1][0] != '*') or  ((pole[0][0] == pole[0][1] == pole[0][2]) and pole[0][2] != '*') or ((pole[2][0] == pole[2][1] == pole[2][2]) and pole[2][0] != '*') or ((pole[0][0] == pole[1][0] == pole[2][0]) and pole[0][0] != '*') or ((pole[0][1] == pole[1][1] == pole[2][1]) and pole[0][1] != '*') or ((pole[0][2] == pole[1][2] == pole[2][2]) and pole[0][2] != '*') or ((pole[0][2] == pole[1][1] == pole[2][0]) and pole[0][2] != '*'):
        return 'X'                            
    else:
        return '*'
def vivod_pole(pole):
    for i in range(3):
        print(*pole[i])

pole = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Игра начинается')
vivod_pole(pole)

kol_for_win = 3
razmer_pole = 3

for turn in range(1, 10):
    col, row = [int(x)-1 for x in input('Введите клетку: ').split()]
    if turn % 2 == 0:
        simv = '0'
    else:
       simv = 'X'
    if pole[row][col] != '*':
        while pole[row][col] != '*':
            print('Введите пустую клетку: ')
            col, row = [int(x)-1 for x in input('Введите клетку: ').split()]
        pole[row][col] = simv
    else:
        pole[row][col] = simv
    vivod_pole(pole)
    rezultat = win_or_no(pole)
    if rezultat != '*':
        print(f'Поздравляем побетителя {rezultat}')
        break














