import time
from threading import Thread
from queue import Queue
import I2C_LCD_driver as i2c_lcd

def set_lcd(q):
    lcd = i2c_lcd.lcd()
    while True:
        lcd.lcd_display_string(q.get(), 1);
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    thr = Thread(target=set_lcd, args=(q,))
    thr.setDaemon(True)
    thr.start()
    for i in range(10):
        q.put(f"test {i}")
        time.sleep(0.5)
