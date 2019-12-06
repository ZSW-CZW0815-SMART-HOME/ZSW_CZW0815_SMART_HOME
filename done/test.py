import time, signal, sys, os
from threading import Event, Thread
from queue import Queue
import RPi.GPIO as GPIO
import lcd, key, rfid, reset, blinds
import utils as u

PIN_HEATER = 6
PIN_ACOND = 13
PIN_LIGHTS = 19

def start_thread(fun, q):
    thr = Thread(target=fun, args=(q,))
    thr.setDaemon(True)
    thr.start()
    threads.append(thr)

def sigend(sig, fram):
    q.join()
    q_lcd.join()
    GPIO.cleanup()
    sys.exit(0)

threads = []

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    signal.signal(signal.SIGINT, sigend)
    GPIO.setup(PIN_HEATER,  GPIO.OUT, initial=GPIO.LOW) 
    GPIO.setup(PIN_ACOND,   GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_LIGHTS,  GPIO.OUT, initial=GPIO.LOW)
    #init
    #thread:
    #   temp
    
    q_lcd = Queue()
    q = Queue()
    start_thread(lcd.set_lcd, q_lcd)
    start_thread(rfid.rfid, q)
    start_thread(key.keyboard, q)
    start_thread(reset.reset, q)

    while True:
        msg = q.get()

        if msg['src'] == 'keyboard':
            key = msg['val']
            if key == 'c':
                q_lcd.put(' '*len(u.code))
                u.code = ""
            elif key == 'a':
                u.check_code(q_lcd)
            elif key == "f1":
                q.put({'src': 'temp', 'val': 50})
            elif key == "f2":
                q.put({'src': 'temp', 'val': -50})
            elif key == "f3":
                q.put({'src': 'temp', 'val': 20})
            elif key == "f4":
                os.spawnl(os.P_NOWAIT, '/usr/bin/python2.7', 'python2.7', 'mail/demo.py')
            else: #if numeric
                if len(u.code) > 8:
                    q_lcd.put(' '*len(u.code))
                    u.code = ""
                else:
                    u.code += key
                    q_lcd.put('*'*len(u.code))

        elif msg['src'] == 'rfid':
            u.check_id(msg['val'], q_lcd)

        elif msg['src'] == 'temp':
            op = u.check_temperature(msg['val'])
            if op == 1:
                GPIO.output(PIN_HEATER, GPIO.LOW)#heat  off
                GPIO.output(PIN_ACOND, GPIO.LOW)#acond on
                pass
            elif op == -1:
                GPIO.output(PIN_HEATER, GPIO.HIGH)#heat  on
                GPIO.output(PIN_ACOND, GPIO.HIGH)#acond off
                pass
            else:
                GPIO.output(PIN_HEATER, GPIO.LOW)#heat  off
                GPIO.output(PIN_ACOND, GPIO.HIGH)#acond off
                pass

        elif msg['src'] == 'reset':
                GPIO.output(PIN_HEATER, GPIO.LOW)#heat  off
                GPIO.output(PIN_ACOND, GPIO.HIGH)#acond off
                GPIO.output(PIN_LIGHTS, GPIO.LOW)
                blinds.blinds("down")

        q.task_done()
