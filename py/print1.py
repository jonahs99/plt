import serial
import time

# device = '/dev/ttyUSB0'
device = '/dev/ttyACM0'

def send(s):
    print('sending', s)
    ser.write(s.encode('utf-8'))

def wait_for_ok():
    ser.write('\r\n\r\n'.encode('utf-8'))
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        print('read', line, flush=True)
        if line.startswith('ok'):
            # while ser.in_waiting > 0:
            #     line = ser.readline().decode('utf-8').rstrip()
            #     print('read', line, flush=True)
            break

ser = serial.Serial(device, 250000)

time.sleep(2)

recv = 0

import sys
for line in sys.stdin:
    print(ser.in_waiting)
    while ser.in_waiting:
            print('read', ser.readline().decode('utf-8').strip())
            # num = int(ser.readline().decode('utf-8'))
            # if num != recv + 1:
            #     print('GOT {} AFTER {}'.format(num, recv))
            # recv = num

            # if num % 1000 == 0:
            #     print(num)
        # wait_for_ok() # wait for a response

    line = line.split(';')[0].rstrip()
    if line:
        send(line + '\r\n')

ser.close()

