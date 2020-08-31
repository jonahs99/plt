import math
import random

revs = 100
s = 3

da = 2 * math.pi / 6
a0 = 0

min_speed = 500
max_speed = 4000
ramp_revs = 8

def to(x, y, f=1000):
    print('G1F{:.0f}X{:.1f}Y{:.1f}'.format(f, x, y))

print('M211 S0')
print('G92 X0 Y0')

a = a0
while a < 2 * math.pi * revs:
    r = a / 2 / math.pi * s

    x = math.cos(a) * r
    y = math.sin(a) * r

    f = (r / s / ramp_revs) * (max_speed - min_speed) + min_speed
    f = min(f, max_speed)

    to(x, y, f)

    a += da

