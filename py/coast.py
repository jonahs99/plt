from plod import *
from random import random
import math

r0 = 20
s = 0.5
a = 12
n = 12
nt = 1000

sins = [0]
for i in range(n):
    for j in range(nt):
        th = 2 * math.pi / nt * j

        r = r0 + (i + j/nt) * s
        for k, sin in enumerate(sins):
            r += math.sin(th * 2**k) * sin

        x = r0 - (math.cos(th) * r)
        y = math.sin(th) * r
        go(x, y)
    
    sins.append(a * 2 * (random() - 0.5) / (i + 1) ** 2)
