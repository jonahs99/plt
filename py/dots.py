def to(x, y, f=1000):
    print('G1 F{:.0f} X{:.1f} Y{:.1f}'.format(f, x, y))

def up():
    print('M280 S30')

def down():
    print('M280 S5')

n = 30
s = 1

def dot(x, y):
    to(x, y)
    down()
    up()

skip = 0

up()
for i in range(n):
    for j in range(n):
        k = (j if i % 2 == 0 else (n-1-j)) 

        y = s * (i - (n-1)/2)
        x = s * (k - (n-1)/2)
        if k % (skip + 1) == 0:
            dot(x, y)

    skip += 1

