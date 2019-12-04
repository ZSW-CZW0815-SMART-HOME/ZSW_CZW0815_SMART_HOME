import time, sys, signal
from threading import Thread
from queue import Queue
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def rfid(q):
    reader = SimpleMFRC522()
    while True:
        card_id = reader.read_id()
        q.put({'src': 'rfid', 'val': card_id})
        time.sleep(0.1)

if __name__ == "__main__":
    def sig_end(sig, frame):
        q.join()
        GPIO.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_end)
    q = Queue()
    thr = Thread(target=rfid, args=(q,))
    thr.setDaemon(True)
    thr.start()
    while True:
        print(type(q.get()['val']), q.get()['val'])
        q.task_done()
