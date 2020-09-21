isup = True
def to(x, y):
    a = x + y
    b = x - y
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



# return to the origin
up()
to(0, 0)
