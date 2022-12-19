#Task_1
def func(x):
    """Функция преобразования строк в байт коды"""
    mas = []
    for i in range(len(x)):
        """Цикл преобразует строки в байт коды
            и заполняет ими пустой список mas[]"""
        c = x[i].encode('utf-8')
        mas.append(c)
    return mas
def func_2(x):
    """Функция преобразования байт кодов в строки"""
    mas = []
    for i in range(len(x)):
        """Цикл преобразует байт коды в строки
            и заполняет ими пустой список mas[]"""
        q = x[i].decode('utf-8')
        mas.append(q)
    return mas
lst = []
try:
    """Обработка неподходящей переменной k"""
    k = int(input('Введите целую цифру того, сколько элементов вы хотите добавить в список: '))
    for i in range(k):
        """Заполняем массив данными для будущей обработки функциями"""
        i = input(f'Введите нужный(-ые) символ(-ы) в {i+1} элемент массива: ')
        lst.append(i)
    print(f'Ваш входной массив: {lst}')
    print(f'Закодированный массив: {func(lst)}\nДекодированный массив: {func_2(func(lst))}')
except ValueError:
    print('Нужно вводить целое положительное число!\nЗапусти еще раз.')

#Task_2
def main():
    """Функция нахождения молекулы спирта

        Переменные:
        file -- создаём файл в который запишем цифры юзера
        input_file -- тот же file, но теперь отдадим его на вход аргументов функции
        output_file -- создаём файл, в который запишем ответы функции

        """
    file = open('inGachi.txt','w+')
    input_file = open('inGachi.txt', 'w+')
    output_file = open('outGachi.txt', 'w+')
    try:
        """Получаем цифры юзера"""
        c = int(input('Введите кол-во атомов С: '))
        h = int(input('Введите кол-во атомов H: '))
        o = int(input('Введите кол-во атомов O: '))
        print('ВНИМАНИЕ!!!\nПрограмма создала 2 файла:\ninGachi.txt и outGachi.txt')
        if c >= 0 and h >=0 and o>=0:
            """Заполняем ими входной файл"""
            s = str(c)+' '+str(h)+' '+str(o)
            file.write(s)
            file.close()
            """Считываем данные из файла и считаем результат"""
            line = input_file.readline().split()
            input_file.close()
            print(f'Введенные вами данные: {line}')
            C, H, O = int(line[0]), int(line[1]), int(line[2])
            c = C//2
            h = H//6
            o = O//1
            ans = min(c, h, o)
            print(f'Ответ: {ans}')
            """Записываем результат в новый файл"""
            output_file.write(f'Ответ: {str(ans)}')
            output_file.close()
        else:
            print('Числа должны быть положительными и целыми!') 
    except ValueError:
        print("Нужно вводить положительное целое число!")
if __name__ == '__main__':
    main()

#Task_3
def main():
    """Функция XOR шифрования"""
    file = open('somedad.txt','w+')
    print()
    text = input('Введите что-нибудь для кодирования.\nВаша строка: ')
    try:
        """Обработка ошибки ключа"""
        key = int(input('Введите ключ - целое число.\nВаш ключ: '))
    except ValueError:
        print('Надо ввести ЦЕЛОЕ ЧИСЛО!')
        if __name__ == '__main__':
            main()
    """Подаём данные юзера в инпут файл(file)"""
    file.write(text)
    file.close()
    file = open('somedad.txt', 'r')
    """Получаем из инпут файла данные"""
    kek = file.readline()
    file.close()
    crypt = ''
    
    try:   
        for i in kek:
            """Шифруем строку юзера"""
            try:
                crypt += chr(ord(i)^ord(key))
            except TypeError:
                crypt += chr(ord(i)^key)
        decrypt=''
        for j in crypt:
            """Дешифруем зашифрованную строку"""
            try:
                decrypt += chr(ord(j)^ord(key))
            except TypeError:
                decrypt += chr(ord(j)^key)
        """Записываем результат функции в файл"""
        file = open('somedad.txt', 'w')
        file.writelines(f'\nВаша исходная строка: {text}\nЗашифрованная строка: {crypt}\nРасшифрованная строка: {decrypt}')
        file.close()
        file = open('somedad.txt', 'r')
        ans = file.read()
        print(ans)
        print('Программа использует somedad.txt, советую удалить его после окончания работы с программой :)')
    except ValueError:
        print('Ошибка ключа. Начните, пожалуйста, заново с ключом = целому положительному числу, желательно не более 1100000 :(')
if __name__ == '__main__':
    main()