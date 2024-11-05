# Домашнее задание по теме "Асинхронность на практике"

import asyncio
from time import sleep

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
       delay = 1 / power
       await asyncio.sleep(delay)
       print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Kate', 2))
    task2 = asyncio.create_task(start_strongman('Kirill', 10))
    task3 = asyncio.create_task(start_strongman('Roma', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())



