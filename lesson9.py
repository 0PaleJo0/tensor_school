#Task_1 from lesson2
def op(a, b):
    m = []
    m.append(a + b)
    m.append(a - b)
    m.append(a*b)
    m.append(a/b)
    m.append(a**b)
    m.append(a%b)
    m.append(a//b)
    return m

def name(n):
    return n

def string(s):
    return s[:-3:-1]
print(string('Igor'))
import math

def rad(r):
    return math.pi * (r**2)

#Task_2
#2.1
def password(s):
    k = 0
    b = False
    if len(s) < 6:
        print('False\nПароль должен содержать 6 или более символов!')
        return b
    for i in s:
        if i.isdigit():
            k += 1
    else:    
        if s.lower() == "password":
            print("False\nПароль не может состоять из слова password!")
            return b
        elif s.isdigit() == True:
            print("False\nПароль не может состоять только из цифр!")
            return b
        elif k == 0:
            print("False\nВ пароле должна быть минимум 1 цифра!")
            return b
        elif k > 0:
            b=True
            print("True\nПароль принят!")
        return b