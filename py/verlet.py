from plod import *
import math

X = [0, 0]
V = [2, 1]
A = [0, 0]

dt = 1/40

n_springs = 2
springs = [
    [10, [10*math.sin(math.pi*2/n_springs*i), 10*math.cos(math.pi*2/n_springs*i)]]
    for i in range(n_springs)
]

def a(X):
    A1 = [0, 0]
    for g, p in springs:
        mag = sum((p[i] - X[i]) ** 2 for i in range(len(X))) ** (1/2)
        m = 1/mag**2
        for i in range(len(X)):
            X[i] += g * (p[i] - X[i]) * m
    return A1

while True:
    go(X[0], X[1])

    for i in range(len(X)):
        X[i] += V[i]*dt + 1/2*A[i]*dt**2

    # calc A1
    A1 = a(X)

    for i in range(len(V)):
        V[i] += 1/2*(A[i] + A1[i])*dt

    A = A1

