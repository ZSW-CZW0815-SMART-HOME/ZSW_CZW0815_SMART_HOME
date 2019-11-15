import socket
import signal
import sys

PORT = 50100

loop = True

def end(sig, frame):
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, end)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen()
while loop:
    conn, addr = s.accept()
    typ = repr(conn.recv(4))
    print(typ)
    with conn:
        while True:
            data = int.from_bytes(conn.recv(1), 'big')
            try:
                if data == 15:
                    conn.sendall(b'nak');
                else:
                    conn.sendall(b'ack');
            except:
                break;
            if data == 10:
                print('exit')
                loop = False
            if data == 15:
                break
            print('rec: ', data)
    print('disconnected')
s.close()
