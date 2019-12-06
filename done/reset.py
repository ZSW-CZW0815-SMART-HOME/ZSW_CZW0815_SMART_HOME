import time, sys, signal
from threading import Thread
from queue import Queue
import RPi.GPIO as GPIO

PIN_RESET = 12

def reset(q):

    def clb(pin):
        q.put({'src': 'reset', 'val': None})

    GPIO.setup(PIN_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN_RESET, GPIO.RISING,
            callback=clb, bouncetime=300)
    while True:
        pass

if __name__ == "__main__":
    def sig_end(sig, frame):
        q.join()
        GPIO.cleanup()
        sys.exit(0)

    GPIO.setmode(GPIO.BCM)
    signal.signal(signal.SIGINT, sig_end)
    q = Queue()
    thr = Thread(target=reset, args=(q,))
    thr.setDaemon(True)
    thr.start()
    while True:
        print(q.get()['val'])
        q.task_done()
