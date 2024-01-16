from plod import *

go(-50, 0, 5000)
for i in range(0, 100):
    go(i-50, 0, 3000)

go(-50, 0, 5000)
go(50, 0, 3000)
go(0, 0, 5000)

