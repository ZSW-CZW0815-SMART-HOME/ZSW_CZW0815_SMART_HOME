from threading import Thread
from queue import Queue
from mfrc522 import SimpleMFRC522

def rfid(q):
    reader = SimpleMFRC522()
    while True:
        card_id = reader.read_id()
        q.put({'src': 'rfid', 'val': card_id})

if __name__ == "__main__":
    q = Queue()
    thr = Thread(target=rfid, args=(q,))
    thr.setDaemon(True)
    thr.start()
    while True:
        print(q.get()['val'])
        q.task_done()
