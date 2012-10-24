import random

def d(die):
    return random.randint(1, die)

def xdy(x,y):
    return sum(d(y) for i in range(x))
