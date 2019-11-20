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

if __name__ == '__main__':
    #init
    #thread:
    #   temp
    #   lcd
    #   key
    #   rfid
    sys.exit(0)
    q = Queue()

    while True:
        msg = q.get()
        if msg['src'] == 'keyboard':
            #check
            pass
        elif msg['src'] == 'rfid':
            #check
            pass
        elif msg['src'] == 'temperature':
            #check
            pass
        q.task_done()
