'''#Task_1
def password(s):
    k=0
    if len(s) < 6:
        print('False\nПароль должен содержать 6 или более символов!')
        password(input("Введите пароль: "))
    for i in s:
        if i.isdigit():
            k+=1
    else:    
        if s.lower() == "password":
            print("False\nПароль не может состоять из слова password!")
            password(input("Введите пароль: "))
        elif s.isdigit() == True:
            print("False\nПароль не может состоять только из цифр!")
            password(input("Введите пароль: "))
        elif k==0:
            print("False\nВ пароле должна быть минимум 1 цифра!")
            password(input("Введите пароль: "))
        elif k>0:
            print("True\nПароль принят!")

password(input("Введите пароль: "))
'''
'''
#Task_2
def func(*args):
    c=0
    for i in args:
        c+=i
    return c
lst=[]
try:
    k = int(input('Введите какое кол-во элементов для суммы вы хотите ввести: '))
    if k<0:
        print('Нужно вводить целое,положительное число!\nЗапустите программу заново.')
        
    for i in range(k):
        i = int(input(f'Введите {i+1} элемент: '))
        lst.append(i)
        print(f'Сумма введенных элементов: {func(*lst)}')
except ValueError:
    print("Вводить нужно числа!\nЗапустите программу еще раз.")
'''
'''#Task_3
try:
    def f(x):
            if x in (1, 2):
                return 1
            return f(x-1) + f(x-2)
    try:
        i=int(input('Введите какое число Фибоначчи вы хотите узнать: '))
        print(f'{i}-ое число Фибоначчи это {f(i)}')
    except ValueError:
        print("Вводить нужно целые числа!")
except KeyboardInterrupt:
    print("\nВы прервали программу.")
    '''