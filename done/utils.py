import os
import json
import sys, time
#import common

lpath = 'home/pi/Desktop/zsw/git/done/'

conf = {'code': "1234", 'cards': [72046226359, 405839336734], 'temp_max': 35, 'temp_min': 10, 'email': 'zsw.projekt.test@gmail.com'} 

code = ""
wcounter = 0

def check_code(q_lcd):
    global code
    global conf
    global wcounter
    q_lcd.put(' '*len(code))
    if code == conf['code']:
        correct_auth(q_lcd)
        q_lcd.put("open")
    else:
        incorrect_auth(q_lcd)
        wcounter += 1
        q_lcd.put("wrong code")
    code = ""
    time.sleep(1)
    q_lcd.put("          ")

def check_id(cid, q_lcd):
    global conf
    if cid in conf['cards']:
        correct_auth(q_lcd)
        q_lcd.put("open")
#   else:
        #stop timeout
    code = ""
    time.sleep(1)
    q_lcd.put("    ")

def check_temperature(temperature):
    '''
    Checks if temperature is outside set range

    Args:
        temp(float): current temperature

    Returns:
        diff(int): too hot(1) | perfect(0) | too cold(-1)

    '''
    global conf
    if temperature > conf['temp_max']: #too hot
        return 1
    elif temperature < conf['temp_min'] : #too cold
        return -1
    else: #perfect
        return 0

def load_configuration(name):
    '''
    Load configuration from file (temperature range, 
    code, card id list, temperature sensors names, 
    mail)

    Args:
        name(string): file name

    Returns:
        conf(dic): configuration info
    '''
    #global data
#   with open(name) as json_file:
#       common.data = json.load(json_file)
    # print(common.data['code'])
    # print(common.data['mail'])
    pass

def correct_auth(lcd_q):
    global wcounter
    wcounter = 0
    os.spawnl(os.P_NOWAIT, '/usr/bin/python3.7', 'python3.7', 'open_door.py')
    #reset timeout if exist

def incorrect_auth(lcd_q):
    global wcounter
    os.spawnl(os.P_NOWAIT, '/usr/bin/python3.7', 'python3.7', 'alarm.py')
    if wcounter >= 3:
        wcounter = 0
        os.spawnl(os.P_NOWAIT, '/usr/bin/python2.7', 'python2.7', 'mail/demo.py')
#       os.system('./python mail/demo.py')
    #   run thread timeout

