#import the class definition from "email_handler.py" file
from email_handler import Class_eMail
#import common
import sys
sys.path.insert(1, '/home/dominika/ZSW_CZW0815_SMART_HOME/main')
import common
import utils

#set the email ID where you want to send the test email 
# global data
utils.load_configuration()
To_Email_ID = common.data['mail']
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
