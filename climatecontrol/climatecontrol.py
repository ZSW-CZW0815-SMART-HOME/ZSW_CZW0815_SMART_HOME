import os, glob, time
import RPi.GPIO as GPIO

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

def control_climate():

#    os.system('modprobe w1-gpio')
#   os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # lamp
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # fan
    high_temp=30.0
    low_temp=10.0


    GPIO.cleanup()
    temperature = read_temp()
    if temperature > high_temp: #warm
        GPIO.output(6, GPIO.HIGH) 
        GPIO.output(13, GPIO.LOW)
        print("warm")
    if temperature < low_temp : #cold
        GPIO.output(6, GPIO.LOW) 
        GPIO.output(13, GPIO.HIGH) 
        print("cold")
    else: #normal
        GPIO.output(6, GPIO.LOW) 
        GPIO.output(13, GPIO.HIGH)
        print("normal")

if __name__ == "__main__":
        control_climate()
