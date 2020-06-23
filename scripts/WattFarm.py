import SerialSend
from SerialSend import send
from time import sleep


send('Button B', 0.1)
sleep(1)
send('Button B', 0.1)
sleep(1)
# send('Button A', 0.1)
# sleep(1)
# send('Button A', 0.1)
# sleep(3)

month = 0
day = 0


def FixDate(): 
    print("FixDate")
    global month
    global day
    send('HAT TOP', 0.1)
    sleep(0.1)
    day = day + 1
    if day > 20:
        day = 0
        for i in range(20):
            send('HAT BOTTOM', 0.1)
            sleep(0.1)
        
        sleep(0.1)
        send('HAT RIGHT', 0.1)
        send('HAT TOP', 0.1)
        sleep(0.1)
        
        month = month + 1
        if month > 10:
            month = 0
            for i in range(10):
                send('HAT BOTTOM', 0.1)
                sleep(0.1)
            
            sleep(0.1)
            send('HAT RIGHT', 0.1)
            send('HAT TOP', 0.1)
            sleep(0.1)

    
    
    for i in range(6):
        send('BUTTON A', 0.1)
        sleep(0.2)

def ClaimReward():
    print("ClaimReward")
    send('BUTTON A', 0.1)
    sleep(1)
    for i in range(10):
        send('BUTTON B', 0.1)
        sleep(0.5)

def OpenDen():
    print("OpenDen")
    send('BUTTON A', 0.1)
    sleep(1)
    send('BUTTON A', 0.1)
    sleep(1)
    send('BUTTON A', 0.1)
    sleep(4)

def OpenTime():
    print("OpenTime")
    send('BUTTON HOME', 0.3)
    sleep(1)
    send('HAT BOTTOM', 0.1)
    send('HAT RIGHT', 0.7)
    send('HAT LEFT', 0.1)
    send('BUTTON A', 0.1)
    sleep(1)
    send('HAT BOTTOM', 1.5)
    send('BUTTON A', 0.1)
    sleep(1)
    for i in range(4):
        send('HAT BOTTOM', 0.1)
        sleep(0.2)
    send('BUTTON A', 0.1)
    sleep(1)
    
    for i in range(2):
        send('HAT BOTTOM', 0.1)
        sleep(0.2)

    send('BUTTON A', 0.1)

    


def ExitHome():
    print("ExitHome")
    for i in range(10):
        send('BUTTON B', 0.1)
        sleep(0.2)
    send('BUTTON HOME', 0.3)

def DenCycle():
    print("DenCycle")
    OpenDen()
    sleep(1)
    OpenTime()
    sleep(1)
    FixDate()
    sleep(1)
    ExitHome()

    sleep(1)
    send('BUTTON B', 0.1)
    sleep(1)
    send('BUTTON A', 0.1)

try:
    # OpenTime()
    # sleep(5)
    # ExitHome()

    # sleep(2)
    ClaimReward()

    DenCycle()
    sleep(5)
    while True:
        ClaimReward()
        DenCycle()
        sleep(5)

        
        

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
