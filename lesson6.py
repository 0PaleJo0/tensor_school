#Task_1
def func(x):
    mas=[]
    for i in range(len(x)):
        c=x[i].encode('utf-8')
        mas.append(c)
    return mas
def func_2(x):
    mas=[]
    for i in range(len(x)):
        q=x[i].decode('utf-8')
        mas.append(q)
    return mas
lst=[]
try:
    k=int(input('Введите целую цифру того, сколько элементов вы хотите добавить в список: '))
    for i in range(k):
        i=input(f'Введите нужный(-ые) символ(-ы) в {i+1} элемент массива: ')
        lst.append(i)
    print(f'Ваш входной массив: {lst}')
    print(f'Закодированный массив: {func(lst)}\nДекодированный масив: {func_2(func(lst))}')
except ValueError:
    print('Нужно вводить целое положительное число!\nЗапусти еще раз.')

#Task_2
def main():
    file=open('inGachi.txt','w+')
    input_file=open('inGachi.txt', 'w+')
    output_file=open('outGachi.txt', 'w+')
    try:
        c=int(input('Введите кол-во атомов С: '))
        h=int(input('Введите кол-во атомов H: '))
        o=int(input('Введите кол-во атомов O: '))
        print('ВНИМАНИЕ!!!\nПрограмма создала 2 файла:\ninGachi.txt и outGachi.txt')
        if c>=0 and h>=0 and o>=0:
                s = str(c)+' '+str(h)+' '+str(o)
                file.write(s)
                file.close()
                line = input_file.readline().split()
                input_file.close()
                print(f'Введенные вами данные: {line}')
                C, H, O = int(line[0]), int(line[1]), int(line[2])
                c = C // 2
                h = H // 6
                o = O // 1
                ans = min(c, h, o)
                print(f'Ответ: {ans}')
                output_file.write(f'Ответ: {str(ans)}')
                output_file.close()
        else:
            print('Числа должны быть положительными и целыми!') 
    except ValueError:
        print("Нужно вводить положительное целое число!")
if __name__=='__main__':
    main()

#Task_3
def main():
    file = open ('somedad.txt','w+')
    print()
    text = input('Введите что-нибудь для кодирования.\nВаша строка: ')
    try:
        key = int(input('Введите ключ - целое число.\nВаш ключ: '))
    except ValueError:
        print('Надо ввести ЦЕЛОЕ ЧИСЛО!')
        if __name__=='__main__':
            main()
    file.write(text)
    file.close()
    file = open('somedad.txt', 'r')
    kek = file.readline()
    file.close()
    crypt =''
    #Шифрование
    try:   
        for i in kek:
            try:
                crypt += chr(ord(i)^ord(key))
            except TypeError:
                crypt += chr(ord(i)^key)
        decrypt=''
        #Расшифрование
        for j in crypt:
            try:
                decrypt += chr(ord(j)^ord(key))
            except TypeError:
                decrypt += chr(ord(j)^key)
        file = open ('somedad.txt', 'w')
        file.writelines(f'\nВаша исходная строка: {text}\nЗашифрованная строка: {crypt}\nРасшифрованная строка: {decrypt}')
        file.close()
        file = open('somedad.txt', 'r')
        ans = file.read()
        print(ans)
        print('Програма использует somedad.txt, советую удалить его после окончания работы с программой :)')
    except ValueError:
        print('Ошибка ключа. Начните, пожалуйста, заново с ключом = целому положительному числу, желательно не более 1100000 :(.')
if __name__=='__main__':
    main()