
import math

size = 180
space = 4

def to(x, y, f=4000):
    print('G1 F{:.0f} X{:.1f} Y{:.1f}'.format(f, x, y))

rad = size / 2
for i in range(size // space):
    to(-rad + i * space, -rad)
    to(rad, -rad + (i + 0.25) * space)
    to(rad - (i + 0.5) * space, rad)
    to(-rad, rad - (i + 0.75) * space)

