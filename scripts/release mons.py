#!/usr/bin/env python3
import argparse
import serial
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('port')
args = parser.parse_args()

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    ser.write(f'{msg}\r\n'.encode('utf-8'));
    sleep(duration)
    ser.write(b'RELEASE\r\n');
    ser.write(b'RELEASE\r\n');
    ser.write(b'RELEASE\r\n');

ser = serial.Serial(args.port, 9600)

#send('Button A', 0.1)
sleep(1)
# send('Button A', 0.1)
# sleep(1)
# send('Button A', 0.1)
# sleep(3)
def ResetCursor():
    send('HAT BOTTOM', 2)
    send('HAT RIGHT', 2)
    send('HAT TOP', 0.1)
    send('HAT RIGHT', 2)
    sleep(1)

def RemoveMon():
    send('Button A', 0.1)

    sleep(1)

    send('HAT BOTTOM', 0.7)
    send('HAT TOP', 0.1)

    sleep(0.1)

    send('Button A', 0.1)

    sleep(1)

    send('HAT TOP', 0.1)

    sleep(1)

    send('Button A', 0.1)

    sleep(2)

    send('Button A', 0.1)

def RemoveRow():
    for i in range(6):
        print("")
        print("removing"+ str(i))
        sleep(0.5)
        RemoveMon()
        sleep(0.5)
        if(i<=5):
            send('HAT LEFT', 0.1)

def RemoveBox():
    # Get to bottom right
    ResetCursor()

    for i in range(5):
        print("")
        print("removing row"+ str(i))
        RemoveRow()
        if(i<=3):
            send('HAT TOP', 0.1)
            send('HAT RIGHT', 2)
    sleep(10)

try:
    # while True:
    for i in range(5):
        RemoveBox()
        ResetCursor()
        send('Button R', 0.1)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
