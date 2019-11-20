#def
#   -check_code
#   -check_id
#   -check_temp
#   -blinds
#   -lights

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

def load_conf():
    pass

if __name__ == '__main__':
    q = Queue()
    q.join()
