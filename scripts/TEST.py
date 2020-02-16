import SerialSend
from SerialSend import send
from time import sleep

while True:
    sleep(2)
    send("Button A", 1)
    sleep(2)
    send("Button B", 1)
    sleep(2)
    send("Button B", 1)
    sleep(2)
    send("Button B", 1)