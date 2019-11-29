import time, signal, sys
from threading import Event, Thread
from queue import Queue
import RPi.GPIO as GPIO
import lcd, key, rfid
from utils import *

data = {'code': "1234", 'card_id': 72046226359}

def start_thread(fun, q):
    thr = Thread(target=fun, args=(q,))
    thr.setDaemon(True)
    thr.start()

def sigend():
    q.join()
    lcd_q.join()
    gpio.cleanup()
    sys.exit(0)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    signal.signal(signal.SIGINT, sigend)
    #init
    #thread:
    #   temp
    
    q_lcd = Queue()
    q = Queue()
    start_thread(lcd.set_lcd, q_lcd)
    start_thread(rfid.rfid, q)
    start_thread(key.keyboard, q)

    code = ""
    wcounter = 0

    while True:
        msg = q.get()
        if msg['src'] == 'keyboard':
            key = msg['val']
            if key == 'c':
                q_lcd.put(' '*len(code))
                code = ""
            elif key == 'a':
                if check_code(code):
                    q_lcd.put(' '*len(code))
                    correct_auth()
                    code=""
                    q_lcd.put("open")
                else:
                    q_lcd.put(' '*len(code))
                    wcounter += 1
                    incorrect_auth()
                    code=""
                    q_lcd.put("wrong")
                pass
            else: #if numeric
                if len(code) > 8:
                    q_lcd.put(' '*len(code))
                    code = ""
                else:
                    q_lcd.put('*'*len(code))
                    code += key
            pass
        elif msg['src'] == 'rfid':
            if check_id(msg['val']):
                correct_auth()
                q_lcd.put(' '*len(code))
                q_lcd.put("open")
                code=""
                #lcd("open")
            else:
                incorrect_auth()
                q_lcd.put(' '*len(code))
                q_lcd.put("wrong")
                code=""
        elif msg['src'] == 'temperature':
            op = check_temperature(msg['val'])
            if op == 1:
                GPIO.output(6, GPIO.LOW)#heat  off
                GPIO.output(13, GPIO.HIGH)#acond on
                pass
            elif op == -1:
                GPIO.output(6, GPIO.HIGH)#heat  on
                GPIO.output(13, GPIO.LOW)#acond off
                pass
            else:
                GPIO.output(6, GPIO.LOW)#heat  off
                GPIO.output(13, GPIO.LOW)#acond off
                pass
        q.task_done()
