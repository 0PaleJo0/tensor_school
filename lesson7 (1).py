#Task_4
import os

def main():
    os.system('clear')
    print(f'Имя текущей операционной системы: {os.name}')
    print(f'Имя текущего пользователя: {os.getlogin()}')
    print(f'Содержание текущего каталога: {os.listdir()}')
if __name__== '__main__':
    main()

#Task_5
import numpy as np
def main():
    arr = np.random.randint(0, 100, size = (3, 3))
    print(f'Исходный сгенерированный массив:\n{arr}')
    print(f'Транспонированный массив:\n{np.transpose(arr)}')
if __name__ == '__main__':
    main()

#Task_6
import modul
print('Пример подключенных функций')
print(modul.gachi(5,6))
print(modul.negachi(5,6))
