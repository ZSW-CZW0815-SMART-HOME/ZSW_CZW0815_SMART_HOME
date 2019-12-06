import RPi.GPIO as GPIO 
from time import sleep 

PIN_LED_ALARM = 26
PIN_BUZZER = 5

def alarm():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(PIN_LED_ALARM, GPIO.OUT, initial=GPIO.LOW) # LED
    GPIO.setup(PIN_BUZZER,    GPIO.OUT, initial=GPIO.LOW) # buzzer
    
    for i in range(3):
        GPIO.output(PIN_LED_ALARM, GPIO.HIGH) # Turn on LED 
        GPIO.output(PIN_BUZZER,    GPIO.HIGH) # Turn on buzzer
        sleep(0.1) 
        GPIO.output(PIN_LED_ALARM, GPIO.LOW) # Turn off buzzer
        GPIO.output(PIN_BUZZER, GPIO.LOW) # Turn off buzzer
        sleep(0.1) 
    GPIO.cleanup()

alarm()
