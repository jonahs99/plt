from plod import *
import math
from random import random

import sys
sys.setrecursionlimit(2**16)

L = 120
dl = 0.1
w = 0.4

lamb_perish = 1/L
lamb_wander = 1/5
lamb_branch = 1/25

def tree(l, a):
    if l <= 0:
        go(0, 0)
        return

    if sampexp(lamb_wander) < dl:
        a = (a + 0.25*(random() - 0.5)) / 2

    go(-w/2, 0)
    with save():
        mov(0, dl)
        rot(a * dl)

        if sampexp(lamb_branch) < dl:
            scl(0.9, 0.9)
            tree(l - dl, a - 0.05)
            tree(l - dl, a + 0.05)
        else:
            tree(l - dl, a)
    go(w/2, 0)

def sampexp(lamb):
    return -1/lamb*math.log(random())

tree(L, 0)

