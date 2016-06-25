import sys, os
import serial

s = serial.Serial('COM4', 9600)

pub = None

while True:
    line = s.readline().strip()
    cmd, param = line.split(' ', 1)
    if cmd == 'PUB':
        pub = param
    elif cmd == 'POS':
        lat, lng = [ float(x) for x in param.split(', ') ]
        print lat, lng
