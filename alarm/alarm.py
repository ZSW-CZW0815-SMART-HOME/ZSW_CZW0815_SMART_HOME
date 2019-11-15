import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # LED
GPIO.setup(28, GPIO.OUT, initial=GPIO.LOW) # buzzer

while True:
    GPIO.output(28, GPIO.HIGH) # Turn on LED 
    GPIO.output(26, GPIO.HIGH) # Turn on buzzer
    sleep(1) 
    GPIO.output(28, GPIO.LOW) # Turn off LED
    sleep(1) 