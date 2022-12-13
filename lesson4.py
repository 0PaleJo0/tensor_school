'''#Task_1
from random import randint
#создание массива и заполнение
m = []
n=15
for i in range(n):
    m.append(randint(0,150))
print('Создал массив из 15 элементов, которые являются рандомными от 0 до 150, и заполнил ими массив:')
print(m)
#сортировка созданного массива
for i in range(n-1):
    for k in range(n-i-1):
        if m[k] > m[k+1]:
            m[k], m[k+1] = m[k+1], m[k]
print('Отсортировал массив методом "Пузырька":')
print(m)
'''
'''#Task_2
d = {"red":(255,0,0,),"green":(0,128,0,),"blue":(0,0,255,)}
print('Создал структуру dict со значениями ключей tuple:')
print(d,'\nПроверка типов:')
print(f'Тип используемой структуры данных: {type(d)}')
print(f'Тип значения ключа red: {d["red"]} = {type(d["red"])}')
print(f'Тип значения ключа green: {d["green"]} = {type(d["green"])}')
print(f'Тип значения ключа blue: {d["blue"]} = {type(d["blue"])}')
'''
'''#Task_3
from random import randint
space_1 = set()
space_2 = set()
#Создание сет-ов с рандомными числами
for i in range(10):
    space_1.add(randint(0,100))
    space_2.add(randint(0,100))
print(f'1-ое множество: {space_1}\n2-ое множество: {space_2}')
print(f'Общие элементы множеств: {space_1 & space_2}')
print(f'Элементы 1-ого, но не 2-ого:{space_1 - space_2}')
print(f'Элементы 2-ого, но не 1-ого:{space_2 - space_1}')
print(f'Элементы, не входящие в оба множества одовременно:{space_1 ^ space_2}')
'''
#Task_4
inventory = dict()
s =int(1)
max = float(20)
print('\nПривет! Это твой инвентарь, написанный гавнокодом.\nМаксимальная вместительность инвентаря 20 кг, ибо ты явно не качал физические скиллы...')
while s != 0:
    print('\n0-выйти из инвентаря 1-посмотреть инвентарь 2-добавить вещь 3-удалить вещь')
    total = sum(inventory.values())
    print(f'В инвентаре свободно {max} кг')
    s = int(input('Что ты хочешь сделать? (Введи нужное тебе значение)\n'))
    if s == 1:
        if len(inventory) == 0:
            print(f'\nТвой инвентарь пустой :(\nМожет что-то в него добавишь?') 
        else:
            print('\nТвой инвентарь: ')
            for key, value in inventory.items():
                print(f'Название вещи: {key} Вес:{value}кг')
    elif s == 2:
        if  max <= 0:
            print('Нет места')
        else:
            name = input('\nВведи имя шмотки: ')
            m = float(input('Введи массу шмотки: '))
            if max-m >=0 and m>0 :
                if name in inventory:
                    print('Увы, но ещё одну шмотку такого же названия нельзя класть в инвентарь, сорян... ')
                else:
                    max-=m
                    inventory[f"{name}"] = m
                    print('Ты положил шмотку в инвентарь! :) ')
            else:
                print('Кек, такую вещь не положить \(0_0)/')
    elif s == 3:
        if len(inventory) == 0:
            print(f'\nТвой инвентарь пустой :(\nМожет что-то в него добавишь?')
        else: 
            print('\nТвой инвентарь: ')
            for key, value in inventory.items():
                print(f'Название вещи: {key} Вес:{value}кг')
            name = input('\nОт чего хочешь избавиться?\nВведи имя вещи: ')
            p=inventory[f"{name}"]
            del inventory[f"{name}"]
            max+=p
            print('Ты удалил эту безнадёжную кладь! ~(o_o)~\n')