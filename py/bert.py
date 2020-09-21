import math

isup = True
def to(x, y):
    a = x#x + y
    b = y#x - y
    f = 4000 if isup else 1000
    print('G1 F{:.0f} X{:.2f} Y{:.2f}'.format(f, a, b))
def up():
    global isup
    isup = True
    print('M280 S30')
def down():
    global isup
    isup = False
    print('M280 S5')

angle = 0
pos = (0, 0)
def turn(deg):
    global angle
    angle += deg / 180 * math.pi
def forward(dist):
    global pos, angle
    x, y = pos
    pos = (x + dist * math.cos(angle), y + dist * math.sin(angle))
    x, y = pos
    to(x, y)

L = {
    'A': '− B F + A F A + F B −',
    'B': '+ A F − B F B − F A +',
}
dist = 1

def lsystem(L, str, n):
    if n <= 0:
        return
    for char in str:
        if char == 'F':
            forward(dist)
        elif char == '-':
            turn(90)
        elif char == '+':
            turn(-90)
        elif char in L:
            lsystem(L, L[char], n-1)

to(0, 0)
lsystem(L, 'A', 3)

# return to the origin
up()
to(0, 0)
