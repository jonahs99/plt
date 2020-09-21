import math
import random

isup = True

def to(x, y):
    a = x + y
    b = x - y
    f = 4000 if isup else 1000
    print('G1 F{:.0f} X{:.1f} Y{:.1f}'.format(f, a, b))

def up():
    global isup
    isup = True
    print('M280 S30')

def down():
    global isup
    isup = False
    print('M280 S5')

n = 10
r = 3
s = 12

seed = random.randrange(1000000)

def poly(x, y, sides, rand):
    random.seed(sides + seed)
    ds = [r * (1 + (rand * random.uniform(-1, 1))) for i in range(sides)]

    for i in range(sides + 1):
        d = ds[i % sides]
        t = i * 2 * math.pi / sides + math.pi/2
        to(x + math.cos(t) * d, y + math.sin(t) * d)
        if i == 0:
            down()
    up()

up()
for i in range(n):
    for j in range(n):
        row = i
        col = j if i % 2 == 0 else (n - 1 - j)

        x = (col - (n-1)/2) * s
        y = (row - (n-1)/2) * s
        sides = col + 3
        rand = (i / n)
        poly(x, y, col + 3, rand)
to(0, 0)

