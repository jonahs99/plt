import serial
import time

# device = '/dev/ttyUSB0'
device = '/dev/ttyACM0'

def send(s):
    # time.sleep(0.01)
    print('sending', s, flush=True)
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

import sys
for line in sys.stdin:
    line = line.split(';')[0].rstrip()
    if line:
        send(line + '\r\n')

        # wait_for_ok() # wait for a response

ser.close()

