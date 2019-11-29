import time, signal, sys
from threading import Event, Thread
from queue import Queue
import RPi.GPIO as GPIO
import lcd, key, rfid
import utils as u

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
    #init
    #thread:
    #   temp
    
    q_lcd = Queue()
    q = Queue()
    start_thread(lcd.set_lcd, q_lcd)
    start_thread(rfid.rfid, q)
    start_thread(key.keyboard, q)

    while True:
        msg = q.get()

        if msg['src'] == 'keyboard':
            key = msg['val']
            if key == 'c':
                q_lcd.put(' '*len(u.code))
                u.code = ""
            elif key == 'a':
                u.check_code(q_lcd)
            else: #if numeric
                if len(u.code) > 8:
                    q_lcd.put(' '*len(u.code))
                    u.code = ""
                else:
                    u.code += key
                    q_lcd.put('*'*len(u.code))

        elif msg['src'] == 'rfid':
            u.check_id(msg['val'], q_lcd)

        elif msg['src'] == 'temperature':
            op = u.check_temperature(msg['val'])
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
