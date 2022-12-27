#Task_1
class Animals:
    def __init__(self, name, group, max_weight, gender):
        self.name = name
        self.group = group
        self.max_weight = max_weight
        self.gender = gender
    def voice(self, text):
        print(text)
Chik = Animals('Chik', 'birds', 40, 'male')
print(Chik.name)
print(Chik.group)
Chik.voice('Ku-ku')
print()

class Mammals(Animals):
    def __init__(self, name, group, max_weight, gender, milk, special_teeth, ears):
        super().__init__(name, group, max_weight, gender)
        self.milk = milk
        self.special_teeth = special_teeth
        self.ears = ears
    def birth_func(self):
        if self.gender == 'Male':
            print('Не может рожать потомство')
        else:
            print('Может рожать потомство')
Mary = Mammals('Mary', 'Mammals', 500, 'Female', 'Yes', 'Yes', 'Yes')
print(Mary.name)
print(Mary.group)
Mary.birth_func()
print()

class Humans(Mammals):
    def __init__(self, name, surname, group, max_weight, gender, 
                milk, special_teeth, ears, weight, high):
        super().__init__(name, group, max_weight, gender, milk, special_teeth, ears)
        self.surname = surname
        self.weight = weight
        self.high = high
    def say_gender(self):    
        if self.gender == 'Female':
            print('Я-женщина')
        else:
            print('Я-мужчина')
Gector = Humans('Gector', 'Abrams', 'Mammals', 160, 'Male', 'No', 'Yes', 'Yes', 85, 185)
Susan = Humans('Susan', 'Abrams','Mammals', 160, 'Female', 'Yes', 'Yes', 'Yes', 55, 170)
print(Susan.name)
print(Gector.name)
Susan.say_gender()
Gector.say_gender()
print()

class Cats(Mammals):
    def __init__(self, name, group, max_weight, gender, 
                milk, special_teeth, ears, cat_home):
        super().__init__(name, group, max_weight, gender, milk, special_teeth, ears)
        self.cat_home = cat_home
    def myau(self):
        print('Мяу')
Hunny = Cats('Hunny', 'Mammals', 40, 'Male', 'No', 'Yes', 'Yes', 'Yes')
print(Hunny.name)
Hunny.myau()
print()

class Dogs(Mammals):
    def __init__(self, name, group, max_weight, gender, 
                milk, special_teeth, ears, collar, dog_food):
        super().__init__(name, group, max_weight, gender, milk, special_teeth, ears)
        self.collar = collar
        self.dog_food = dog_food
    def Waf(self):
        print('Гав-гав')
Luddy = Dogs('Luddy', 'Mammals', 60, 'Female', 'Yes', 'Yes', 'Yes', 'Flea collar', 'Yes')
print(Luddy.name)
Luddy.Waf()
print()

#Task_2
class Student(Humans):
    def __init__(self, name, surname, group, max_weight, gender, milk, 
                special_teeth, ears, weight, high, HW_count):
        super().__init__(name, surname, group, max_weight, gender, milk, 
                        special_teeth, ears, weight, high)
        self.HW_count = HW_count
#Task_3
    def __lt__(self, other):
        print(self.HW_count < other.HW_count)
George = Student('George', 'Harrison', 'Mammals', 200, 'Male', 
                'No', 'Yes', 'Yes', 75, 175, 8)
Nano = Student('Nano', 'Pentum', 'Mammals', 200, 'Female', 
                'Yes', 'Yes', 'Yes', 50, 170, 12)
George.__lt__(Nano)

#Task_4
import time
import logging
def decorator(func):
    def timecount():
        logging.basicConfig(filename="mySnake.log", level=logging.INFO)
        logging.info("Program started")
        startTime = time.time()
        func()
        endTime = time.time()
        totalTime = endTime - startTime
        print(f'Время выполнения: {totalTime}')
        logging.info(f"{totalTime}\nDone!")
    return timecount
 
@decorator    
def priv():
    print('PRIV')
priv()



