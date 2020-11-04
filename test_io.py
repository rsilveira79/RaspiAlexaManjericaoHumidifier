from gpiozero import LED
from time import sleep

## Definitions
rele = LED("GPIO21")
TURNON_TIME = 10
TURNOFF_TIME = 2

def main_cycle():
    while True:
        turn_water_on()
        print("rele ON")
        sleep(TURNOFF_TIME)

def turn_water_on():
    rele.off()
    sleep(TURNON_TIME)
    rele.on()
    return None

if __name__=='__main__':
    main_cycle()



