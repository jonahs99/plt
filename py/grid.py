import math

def to(x, y, f=1000):
    print('G1 F{:.0f} X{:.1f} Y{:.1f}'.format(f, x, y))

def up():
    print('M280 S30')

def down():
    print('M280 S5')

n = 10
r = 2
s = 6

def circle(x, y):
    sides = 20
    for i in range(sides):
        t = i * 2 * math.pi / sides
        to(x + math.cos(t) * r, y + math.sin(t) * r)
        if i == 0:
            down()
    up()

up()
for i in range(n):
    for j in range(n):
        circle((i - (n-1)/2) * s, (j - ((n-1)/2)) * s)

