import time
import threading
import socket
import signal
import sys
import RPi.GPIO as GPIO

PORT = 50100

key_row = [17, 27, 22, 0]
key_col = [15, 18, 23, 24]
loop = True
btn_press_event = threading.Event()
key_col_num = 0
key_num = {}

def end(sig, frame):
    s.close()
    GPIO.cleanup()
    sys.exit(0)

def btn_pressed(col_ch):
    global btn_press_event
    global key_col_num
    if btn_press_event.is_set():
        return
    key_col_num = col_ch
    btn_press_event.set()

i = 0
for col in key_col:
    key_num[col] = {}
    for row in key_row:
        key_num[col][row] = i
        i += 1
signal.signal(signal.SIGINT, end)
GPIO.setmode(GPIO.BCM)
for pin in key_row:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
for pin in key_col:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING,
            callback=btn_pressed, bouncetime=300)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', PORT))
s.sendall(b'keyb')

while loop:
    btn_press_event.wait()
    col = -1
    for pin in key_row:
        GPIO.output(pin, GPIO.LOW)
        if GPIO.input(key_col_num) == False:
            col = pin
            break;
    if col >= 0:
        s.sendall((key_num[key_col_num][col]).to_bytes(1, 'big'))
        if s.recv(3) != b'ack':
           s.close()
           GPIO.cleanup()
           sys.exit(0)
        if key_num[key_col_num][col] == 15:
            loop = False
        #print(int.from_bytes((key_num[key_col_num][col]).to_bytes(1, 'big'), 'big'))
    for pin in key_row:
        GPIO.output(pin, GPIO.HIGH)
        if pin == col:
            break;
    time.sleep(0.001)
    btn_press_event.clear()
    #loop = False

GPIO.cleanup()
