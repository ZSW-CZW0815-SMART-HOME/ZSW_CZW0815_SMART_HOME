import os
import json
import sys
import common


def check_code(code):
    if code == common.data['code']:
        print('OK')
    else:
        os.system('python mail/demo.py') # new process
        print('Mail sent')

def check_id(id):
    '''
    Look for id in list of authorized card id's

    Args:
        id(int): card id

    Returns:
        correct(bool): match
    '''
    pass

def check_temperature(temp):
    '''
    Checks if temperature is outside set range

    Args:
        temp(float): current temperature

    Returns:
        diff(int): too hot(1) | perfect(0) | too cold(-1)

    '''
    temperature = temp
    high_temp=30.0
    low_temp=10.0
    if temperature > high_temp: #too hot
        tempResult=1
    elif temperature < low_temp : #too cold
        tempResult=-1
    else: #perfect
        tempResult=0
    return tempResult

def move_blinds(move):
    '''
    Move blinds up/down

    Args:
        move(int): up/down
    '''
    pass

# load to data dictionary in common.py file
def load_configuration(): # ok
    with open('data.json') as json_file:
        common.data = json.load(json_file) 
    
def correct_auth():
    '''

    '''
    global wcounter
    #reset timeout if exist
    #reset "wrong code" counter
    #run process open
    pass

def incorrect_auth():
    '''

    '''
    global wcounter
    #run thread alarm
    #run thread timeout
    #if "wrong code" == 3
    #   run process/thread camera
    pass
