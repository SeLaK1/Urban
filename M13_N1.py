import asyncio

async def start_strongman(name, power):
    print(f'{name} начал соревнования')
    count_shar = 0
    while count_shar < 5:
        await asyncio.sleep(1/power)
        count_shar += 1
        print(f'Силач {name} поднял штангу под номером {count_shar}')
    print(f'Силач {name} закончил соревнования')


async def start_tournament(spisok_ytchasnikov):
    for i in range(len(spisok_ytchasnikov)):
        locals()['task_'+str(i)] = asyncio.create_task(start_strongman(*spisok_ytchasnikov[i]))

    for i in range(len(spisok_ytchasnikov)):
        await locals()['task_'+str(i)]


spisok_ytchasnikov = [['Pasha', 3],
                        ['Denis', 4],
                        ['Apollon', 5]]

asyncio.run(start_tournament(spisok_ytchasnikov))
