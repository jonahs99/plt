from math import *
from plod import *
from random import expovariate, random

width = 50
height = 50
s = 0.5
dl = 0.3

min_dash = 0.6

def density(x, y):
    #return 0.96
    return (x + width/2) / width
    #r2 = (x**2 + y**2) / min(width/2, height/2)**2
    #return 1 - exp(-4*r2)

def depth(x, y):
    return 0
    #r2 = (x**2 + (y/0.577)**2) / (width/2)**2 
    #u = 5*sqrt(r2)
    #return 2 * cos(3*u)/(1+u**2)

def remap(v, a, b, c, d):
    return c + (d-c) * (v-a) / (b-a)

n = int(height // s)

for i in range(n):
    y = i * s - height/2
    x = -width/2

    up()
    is_down = False
    go(x, y, 3000)

    if random() < density(x, y):
        down()
        is_down = True

    while x < width/2:
        d = density(x, y)
        z = depth(x, y)

        if d < 0.5:
            down_scale = min_dash
            up_scale = down_scale * (1/d - 1) if d > 0 else 0
        else:
            up_scale = min_dash
            down_scale = up_scale / (1/d - 1) if d > 0 else 0

        if is_down:
            l = expovariate(1) * down_scale
        else:
            l = expovariate(1) * up_scale

        x += min(l, dl)
        x = min(x, width/2)

        go(x, y - z, 1000)

        if l < dl:
            if is_down:
                up()
                is_down = False
            else:
                down()
                is_down = True

up() 
go(0, 0)

