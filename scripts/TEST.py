import SerialSend
from SerialSend import send
from time import sleep

while True:
    sleep(2)
    send('BUTTON HOME', 10)