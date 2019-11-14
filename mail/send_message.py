import sys
import runpy
import os

# demo input
# if correct - everything is ok
# if incorrect - send warning email
correct_password = 'test'
input = sys.argv[1]

if input == correct_password:
    print('OK')
else:
    os.system('python demo.py')
    print('Mail sent')
