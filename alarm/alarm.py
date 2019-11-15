import RPi.GPIO as GPIO 
from time import sleep 

def alarm():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # LED
    GPIO.setup( 5, GPIO.OUT, initial=GPIO.LOW) # buzzer
    
    for i in range(3):
        GPIO.output(12, GPIO.HIGH) # Turn on LED 
        GPIO.output( 5, GPIO.HIGH) # Turn on buzzer
        sleep(0.5) 
        GPIO.output( 5, GPIO.LOW) # Turn off buzzer
        sleep(0.5) 
    GPIO.cleanup()

if __name__ == "__main__":
    alarm()
