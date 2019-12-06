#import the class definition from "email_handler.py" file
from email_handler import Class_eMail
#import common
import sys
sys.path.append('/home/pi/Desktop/zsw/git/done')
import utils

conf = {'code': "1234", 'cards': [72046226359, 405839336734], 'temp_max': 35, 'temp_min': 10, 'email': 'zsw.projekt.test@gmail.com'} 

#set the email ID where you want to send the test email 
# global data
To_Email_ID = conf['email']
#print(To_Email_ID)

# warning
warning_subject = 'Warning!'
warning_text = 'Warning! \
                The password was incorrect. \
                Please enter the correct password.'

# Send Plain Text Email 
email = Class_eMail()
email.send_Text_Mail(To_Email_ID, warning_subject, warning_text)
del email
