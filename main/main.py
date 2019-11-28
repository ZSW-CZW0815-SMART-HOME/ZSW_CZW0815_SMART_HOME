import time, signal, sys
from threading import Event, Thread
from queue import Queue
import RPi.GPIO as GPIO

import utils

def sigend():
    q.join()
    lcd_q.join()
    gpio.cleanup()
    sys.exit(0)

if __name__ == '__main__':
    #init
    #thread:
    #   temp
    #   lcd
    #   key
    #   rfid
    q = Queue()
    lcd_q = Queue()
    code = ""
    wcounter = 0

    while True:
        msg = q.get()
        if msg['src'] == 'keyboard':
            key = msg['val']
            if key == 'c':
                code = ""
            elif key == 'a':
                if check_code(code):
                    correct_auth()
                    #lcd("open")
                else:
                    wcounter += 1
                    incorrect_auth()
                    #lcd("wrong code")
                pass
            else: #if numeric
                if len(code) > 8:
                    code = ""
                else:
                    #lcd('*')
                    code += key
            pass
        elif msg['src'] == 'rfid':
            if check_id(msg['val']):
                correct_auth()
                #lcd("open")
            else:
                incorrect_auth()
                #lcd("wrong code")
        elif msg['src'] == 'temperature':
            op = check_temperature(msg['val'])
            if op == 1:
                GPIO.output(6, GPIO.LOW)#heat  off
                GPIO.output(13, GPIO.HIGH)#acond on
                pass
            elif op == -1
                GPIO.output(6, GPIO.HIGH)#heat  on
                GPIO.output(13, GPIO.LOW)#acond off
                pass
            else:
                GPIO.output(6, GPIO.LOW)#heat  off
                GPIO.output(13, GPIO.LOW)#acond off
                pass
        q.task_done()