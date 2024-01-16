from plod import *
import math

width = 40
height = 80
s = 0.5

min_speed = 500
max_speed = 10000

n = int(height // s)

up()

with save():
    mov(-width/2, -height/2)
    for i in range(n):
        y = s*i
        speed = min_speed + (max_speed-min_speed)*i/n

        go(0, y, speed)
        down()
        go(width, y, speed)
        up()

go(0, 0)

