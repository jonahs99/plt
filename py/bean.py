import math

def to(x, y):
    a = x + y
    b = x - y
    f = 1500
    print('G1 F{:.0f} X{:.2f} Y{:.2f}'.format(f, a, b))

revs = 100
s = 0.5

dl = 0.01

a = 0
i = 0
while a < 2 * math.pi * revs:
    z = a / 2 / math.pi * s
    r = z * (1 + 0.2 * math.cos(a * 33 * 0.997))

    x = math.cos(a) * r
    y = math.sin(a) * r

    to(x, y)

    a += dl / max(r, 1)
    i += 1
up()
to(0, 0)

