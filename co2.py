#!/usr/bin/python

import sys, serial, time

device = serial.Serial('/dev/ttyAMA0', 38400, timeout=5)

while(True):
    try:
        rcvBuf = bytearray()
        device.reset_input_buffer()
        rcvBuf = device.read_until(size=12)
        print rcvBuf
        temp = rcvBuf.find('p')
        a = rcvBuf[2:temp]
        b = int(a)
        print b
    except Exception as e:
        print("Exception read") + str(e)

    time.sleep(5)


