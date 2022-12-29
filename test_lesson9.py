import lesson9
import math
#Task_1
def test_1():
    a = [3, -1, 2, 0.5, 1, 1, 0]
    assert lesson9.op(1, 2) == a

def test_2():
    assert lesson9.name('Igor') == 'Igor'

def test_3():
    assert lesson9.string('Igor') == 'ro'

def test_4():
    assert lesson9.rad(5) == math.pi * (5**2)

#Task_2
#2.1
def test_5():
    assert lesson9.password('ggggggggg') == False
def test_6():
    assert lesson9.password('!ggffgfg123') == True
def test_7():
    assert lesson9.password('!ggf') == False
def test_8():
    assert lesson9.password('password') == False
