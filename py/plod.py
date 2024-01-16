from contextlib import contextmanager
import math

# column-major
_tf = [1, 1, -1, 1, 0, 0]

@contextmanager
def save():
    global _tf
    prev = _tf
    yield
    _tf = prev
    return

def tf(T):
    global _tf
    b, a = T, _tf
    _tf = [
        a[0]*b[0] + a[2]*b[1],
        a[1]*b[0] + a[3]*b[1],
        a[0]*b[2] + a[2]*b[3],
        a[1]*b[2] + a[3]*b[3],
        a[0]*b[4] + a[2]*b[5] + a[4],
        a[1]*b[4] + a[3]*b[5] + a[5],
    ]
    return 

def mov(x, y):
    return tf([1, 0, 0, 1, x, y])

def rot(a):
    c, s = math.cos(a), math.sin(a)
    return tf([c, s, -s, c, 0, 0])

def scl(sx, sy):
    return tf([sx, 0, 0, sy, 0, 0])

def go(x, y, f=1000):
    u = _tf[0]*x + _tf[2]*y + _tf[4]
    v = _tf[1]*x + _tf[3]*y + _tf[5]
    print('G1 X{:.2f} Y{:.2f} F{:.0f}'.format(u, v, f))

def up():
    print('M280S0')

def down():
    print('M280S12')


