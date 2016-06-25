import sys, os
import serial
import time
import urllib

POS_URL = 'http://wthapp.azurewebsites.net/api/UpdateBusPosition'

s = serial.Serial('COM4', 9600)

time.sleep(5)

s.write("WTH.NAME\r\n")
while True:
    BT_NAME = s.readline().strip()
    print BT_NAME
    if not BT_NAME.startswith('POS'):
        break

pub = None

while True:
    line = s.readline().strip()
    try:
        cmd, param = line.split(' ', 1)
    except:
        print "unknown line:", line
        continue
    if cmd == 'PUB':
        pub = param
    elif cmd == 'POS':
        lat, lng = [ float(x) for x in param.split(', ') ]
        print lat, lng
        u = urllib.urlopen(POS_URL, 'Name=%s&Latitude=%0.6f&Longitude=%0.6f' % (BT_NAME, lat, lng))
        u.read()
        if u.getcode() != 200:
            print u.getcode()
    else:
        print "unknown line:", line
        
