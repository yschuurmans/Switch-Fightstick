import SerialSend
from SerialSend import send
from time import sleep

send('Button A', 0.1)
sleep(1)
# send('Button A', 0.1)
# sleep(1)
# send('Button A', 0.1)
# sleep(3)

def FlyToDaycare():
    ## Fly to daycare
    print("Flying to Daycare")
    sleep(0.1)
    send('Button X', 0.1)
    sleep(1)
    send('HAT RIGHT', 1)
    sleep(0.2)
    send('HAT TOP', 1)
    send('Button A', 0.1)
    sleep(3)
    send('Button A', 0.1)
    sleep(1)
    send('Button A', 0.1)
    sleep(3.5)

try:
    while True:

        # Fly to daycare
        FlyToDaycare()

        # Retrieve egg
        send('LY MAX', 1.5)
        send('LX MIN', 0.1)
        send('Button A', 0.1)
        sleep(2)
        send('Button A', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(2)
        send('Button A', 0.1)
        sleep(3)
        send('HAT BOTTOM', 0.1)
        sleep(1)
        send('Button A', 0.1)
        sleep(3)
        send('Button A', 0.1)
        sleep(2)
        send('Button A', 0.1)
        sleep(2)

        #Get on Bike
        send('Button START', 0.1)
        sleep(1)
        ## Hatch Egg Loop
        #length depends on pokemon hatch rate, add 2 loops for random deviation
        #formula unknown, for calculation: Dreepy: 14
        #formula unknown, for calculation: aegislash: 7
        for i in range(16): 
            print("")
            print("")
            print("Loop" + str(i))
            ## Fly to daycare
            FlyToDaycare()
            # Drive Straigth ahead
            send('LY MIN', 1)
            send('Button B', 0.1)
            send('LY MIN', 7)
            sleep(0.5)
        
        for i in range(10):
            send('Button B', 0.1)
            sleep(1)

        #Get off bike
        send('Button START', 0.1)
        sleep(2)

except KeyboardInterrupt:
    send('RELEASE')
    send('CLOSE')
