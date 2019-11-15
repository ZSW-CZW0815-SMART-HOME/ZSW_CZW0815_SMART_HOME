import os, glob, time
import RPi.GPIO as GPIO
import I2C_LCD_driver
from mfrc522 import SimpleMFRC522


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN) # thermometer
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # lamp
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # fan
highTemp=30.0
lowTemp=10.0



def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        return float(temp_string) / 1000.0


reader = SimpleMFRC522()
mylcd = I2C_LCD_driver.lcd()

tmp = 0
try:
    id = reader.read_id()
finally:
    GPIO.cleanup()
while True:
    temp = read_temp()
    if temp > highTemp: #warm
        GPIO.output(6, GPIO.HIGH) 
        GPIO.output(13, GPIO.LOW) 
    if temp < lowTemp : #cold
        GPIO.output(6, GPIO.LOW) 
        GPIO.output(13, GPIO.HIGH) 
    else: #normal
        GPIO.output(6, GPIO.LOW) 
        GPIO.output(13, GPIO.HIGH) 
    time.sleep(1)
    try:
        id = reader.read_id_no_block()
    finally:
        GPIO.cleanup()
    if id == None:
        break