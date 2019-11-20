#load conf
#create queue
#start threads
#while True
#   switch(q.get)
#   case 'key'
#       check_code
#   case 'rfid'
#       check_rfid
#   case 'temp'
#       check_temp

import time, signal, sys
from threading import Event, Thread
from queue import Queue
import RPi.GPIO as GPIO

import utils

def sigend():
    q.join()
    gpio.cleanup()
    sys.exit(0)

def correct():
    #reset timeout if exist
    #reset "wrong code" counter
    #lcd("open")
    #run process open
    pass

def wrong():
    #run thread alarm
    #run thread timeout
    #if "wrong code" == 3
    #   run process/thread camera
    #lcd("wrong)"
    pass

if __name__ == '__main__':
    #init
    #thread:
    #   temp
    #   lcd
    #   key
    #   rfid
    q = Queue()
    code = ""
    while True:
        msg = q.get()
        if msg['src'] == 'keyboard':
            key = msg['val']
            if key == 'c':
                code = ""
            elif key == 'a':
                if check_code(code):
                    correct()
                else:
                    #increment "wrong code" counter
                    wrong()
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
                correct()
            else:
                wrong()
        elif msg['src'] == 'temperature':
            op = check_temperature(msg['val'])
            if op == 1:
                #heat  off
                #acond on
                pass
            elif op == -1
                #heat  on
                #acond off
                pass
            else:
                #heat  off
                #acond off
                pass
        q.task_done()
