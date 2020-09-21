import math

isup = True
def to(x, y):
    a = x + y
    b = x - y
    f = 4000 if isup else 1000
    print('G1 F{:.0f} X{:.2f} Y{:.2f}'.format(f, a, b))
def up():
    global isup
    isup = True
    print('M280 S30')
def down():
    global isup
    isup = False
    print('M280 S5')

revs = 100
s = 1

dl = 1

ramp_revs = 8

a = 0
i = 0
while a < 2 * math.pi * revs:
    r = a / 2 / math.pi * s

    x = math.cos(a) * r
    y = math.sin(a) * r

    if i % 2 == 0:
        down()
    else:
        up()
    to(x, y)

    a += dl / max(r, 1)
    i += 1
up()
to(0, 0)

