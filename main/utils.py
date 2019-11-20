def check_code():
    '''
    Check combination

    Parameters:
        code(string): code 

    Returns:
        correct(bool): match
    '''
    pass

def check_id():
    '''
    Look for id in list of authorized card id's

    Args:
        id(int): card id

    Returns:
        correct(bool): match
    '''
    pass

def check_temp():
    '''
    Checks if temperature is outside set range

    Args:
        temp(float): current temperature

    Returns:
        diff(int): too hot(1) | perfect(0) | too cold(-1)
    '''
    pass

def move_blinds():
    '''
    Move blinds up/down

    Args:
        dir(int): up/down
    '''
    pass

def load_configuration():
    '''
    Load configuration from file (temperature range, 
    code, card id list, temperature sensors names, 
    mail)

    Args:
        name(string): file name

    Returns:
        conf(dic): configuration info
    '''
