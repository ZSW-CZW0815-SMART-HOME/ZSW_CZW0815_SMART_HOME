import os, glob, time, signal
from threading import Thread
from queue import Queue
import RPi.GPIO as GPIO

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')

def read_temp_raw(dv):
    dv = dv + '/w1_slave'
    f = open(dv, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    temp = []
    for dev in device_folder:
        lines = read_temp_raw(dev)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
        temp.append(float(temp_string) / 1000.0)
    return temp

def temp(q):
    while True:
        q.put({'src': 'temp', 'val': read_temp()})
        time.sleep(1)

if __name__ == "__main__":
    def sig_end(sig, frame):
        q.join()
        GPIO.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_end)
    q = Queue()
    thr = Thread(target=temp, args=(q,))
    thr.setDaemon(True)
    thr.start()
    while True:
        print(q.get()['src'], q.get()['val'])
        q.task_done()
