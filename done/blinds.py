from time import sleep
import RPi.GPIO as GPIO

PIN_BLINDS_UP = 20
PIN_BLINDS_DOWN = 21 

def blinds(mov):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_BLINDS_UP, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_BLINDS_DOWN, GPIO.OUT, initial=GPIO.HIGH)
    if mov == "up":
        GPIO.output(PIN_BLINDS_UP, GPIO.LOW)
        sleep(1)
        GPIO.output(PIN_BLINDS_UP, GPIO.HIGH)
    else:
        GPIO.output(PIN_BLINDS_DOWN, GPIO.LOW)
        sleep(1)
        GPIO.output(PIN_BLINDS_DOWN, GPIO.HIGH)

if __name__ == "__main__":
    blinds("up")
    sleep(1)
    blinds("down")
    GPIO.cleanup()
