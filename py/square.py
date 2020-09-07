def to(x, y, f=4000):
    print('G1F{:.0f}X{:.1f}Y{:.1f}'.format(f, x, y))

while True:
    to(0, 0)
    to(10, 0)
    to(10, 10)
    to(0, 10)

