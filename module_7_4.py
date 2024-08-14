team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
#tasks_total = 82
#time_avg = 45.2
#challenge_result = 'Победа команды Волшебники данных!'

print('В команде %s участников: %s!' % (team1_name, team1_num))
print('В команде %s участников: %s!' % (team2_name, team2_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда {} решила задач: {}!'.format(team1_name, score1))
print('Команда {} решила задач: {}!'.format(team2_name, score2))
print('{} решили задачи за {}с!'.format(team1_name, team1_time))
print('{} решили задачи за {}с!'.format(team2_name, team2_time))
print(f'Команды решили {score1} и {score2} задач.')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = f'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = f'Победа команды Волшебники Данных!'
else:
    result = f'Ничья!'
challenge_result = result
print(f'Результат битвы: {challenge_result}')

tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / (score1 + score2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')

















