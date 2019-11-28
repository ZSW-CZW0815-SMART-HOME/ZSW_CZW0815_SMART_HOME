import time
from threading import Event, Thread
import signal
import sys
from queue import Queue
import RPi.GPIO as GPIO

key_num = {
        15: {17: '1', 27: '2', 22: '3', 0: 'f1'}, 
        18: {17: '4', 27: '5', 22: '6', 0: 'f2'},
        23: {17: '7', 27: '8', 22: '9', 0: 'f3'},
        24: {17: 'a', 27: '0', 22: 'c', 0: 'f4'}
        }



def keyboard(q):

    key_row = [17, 27, 22,  0]
    key_col = [15, 18, 23, 24]
    btn_press_event = Event()
    key_col_num = -1

    def btn_pressed(col_ch):
        nonlocal key_col_num
        if btn_press_event.is_set():
            return
        key_col_num = col_ch
        btn_press_event.set()

    #set gpio
    GPIO.setmode(GPIO.BCM)
    for pin in key_row:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    for pin in key_col:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING,
                callback=btn_pressed, bouncetime=300)
    #main
    while True:
        btn_press_event.wait()
        col = -1
        #find right row
        for pin in key_row:
            GPIO.output(pin, GPIO.LOW)
            if GPIO.input(key_col_num) == False:
                col = pin
                break;
        #result
        if col >= 0:
            q.put({'src': 'keyboard', 'val': key_num[key_col_num][col]})
        #reset changed rows
        for pin in key_row:
            GPIO.output(pin, GPIO.HIGH)
            if pin == col:
                break;
        time.sleep(0.001)
        btn_press_event.clear()



#__main__
if __name__ == "__main__":

    def sig_end(sig, frame):
        q.join()
        GPIO.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_end)
    q = Queue()
    thr = Thread(target=keyboard, args=(q,))
    thr.setDaemon(True)
    thr.start()
    while True:
        print(q.get()['val'])
        q.task_done()
