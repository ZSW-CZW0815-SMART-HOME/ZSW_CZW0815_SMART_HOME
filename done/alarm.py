import RPi.GPIO as GPIO 
from time import sleep 

PIN_LED_ALARM = 1#temp
PIN_BUZZER = 5

def alarm():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(PIN_LED_ALARM, GPIO.OUT, initial=GPIO.LOW) # LED
    GPIO.setup(PIN_BUZZER,    GPIO.OUT, initial=GPIO.LOW) # buzzer
    
    for i in range(3):
        GPIO.output(PIN_LED_ALARM, GPIO.HIGH) # Turn on LED 
        GPIO.output(PIN_BUZZER,    GPIO.HIGH) # Turn on buzzer
        sleep(0.5) 
        GPIO.output(PIN_BUZZER, GPIO.LOW) # Turn off buzzer
        sleep(0.5) 
        GPIO.output(PIN_LED_ALARM, GPIO.LOW) # Turn off LED
    GPIO.cleanup()

if __name__ == "__main__":
    alarm()
