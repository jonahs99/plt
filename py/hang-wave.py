import math
import random

revs = 100
s = 2
w_amp = 2
w_speed = 9
r0 = 6

dl = 0.4

min_speed = 500
max_speed = 2000
ramp_revs = 8

def to(x, y, f=1000):
    print('G1F{:.0f}X{:.1f}Y{:.1f}'.format(f, x, y))

print('M211 S0')
print('G92 X0 Y0')

a = r0 / s * 2 * math.pi
l = 0
while a < 2 * math.pi * revs:
    r = a / 2 / math.pi * s + math.sin(a * w_speed) * w_amp

    x = math.cos(a) * r
    y = math.sin(a) * r

    f = (r / s / ramp_revs) * (max_speed - min_speed) + min_speed
    f = min(f, max_speed)

    to(x, y, f)

    a += dl / max(r, 1)
    l += dl
