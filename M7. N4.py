
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %s!' % 5)
print('Итого сегодня в командах участников: %(team1)s и %(team2)s!' % {'team1': 5, 'team2': 6,})

print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}'.format(team2_time))

print(f'Команды решили {score_1} и {score_2}')
print(f'Результат битвы: победа команды {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round((team1_time + team2_time)/2, 3)} секунды на задачу!')