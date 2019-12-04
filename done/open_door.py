import RPi.GPIO as GPIO 
from time import sleep 

PIN_LED_OPEN = 1
PIN_LOCK = 14

def open_door():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(PIN_LED_OPEN, GPIO.OUT, initial=GPIO.LOW) # LED
    GPIO.setup(PIN_LOCK,     GPIO.OUT, initial=GPIO.LOW) # lock
    
    for i in range(3):
        GPIO.output(PIN_LED_OPEN, GPIO.HIGH) # Turn on LED 
        GPIO.output(PIN_LOCK,     GPIO.HIGH) # Turn on lock
        sleep(1) 
        GPIO.output(PIN_LOCK, GPIO.LOW) # Turn off lock
        GPIO.output(PIN_LED_OPEN, GPIO.LOW) # Turn off LED
    GPIO.cleanup()

open_door()
