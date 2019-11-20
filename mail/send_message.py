import sys
import runpy
import os
import threading

# demo input
# if correct - everything is ok
# if incorrect - send warning email
def init(input):
    correct_password = 'test'
    if input == correct_password:
        print('OK')
    else:
        os.system('python demo.py')
        print('Mail sent')

input = sys.argv[1]
mail = threading.Thread(target=init, args=(input,))
mail.start()
