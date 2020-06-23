import SerialSend
from SerialSend import send
from time import sleep


send('Button B', 0.1)
sleep(1)
send('Button B', 0.1)
sleep(1)

try:
    sleep(5)
    while True:
        send('Button A', 0.1)
        sleep(1)

        
        

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
