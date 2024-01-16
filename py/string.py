from plod import *
import math
from random import random

L = 50
N = 100
H = 6
spacing = 0.5

R = 2
N_smooth = 5
feed = 10000

s = [ [(i-(N-1)/2) * L/(N-1), 0] for i in range(N) ]
v = [ [0, 0] for _ in s ]

for p in s[1:-1]:
    p[0] += R*2*(random() - 0.5)
    p[1] += R*2*(random() - 0.5)

def draw(s):
    for _ in range(N_smooth):
        smoothed = list(s)
        for i in range(1, len(s)-1):
            for k in range(2):
                smoothed[i][k] = 0.25*s[i-1][k] + 0.5*s[i][k] + 0.25*s[i+1][k]

    up()
    go(*smoothed[0], feed)
    down()
    for i, p in enumerate(smoothed[1:]):
        go(*p, feed * (1 - i/N) * ((i+1) / N))
    up()

T = int(H / spacing)

with save():
    mov(0, -H/2)
    for i in range(T):
        draw(s)
        smoothed = list(s)
        for i in range(1, len(s)-1):
            for k in range(2):
                smoothed[i][k] = 0.05*s[i-1][k] + 0.9*s[i][k] + 0.05*s[i+1][k]
        s = smoothed
        mov(0, spacing)

go(0, 0, feed)

