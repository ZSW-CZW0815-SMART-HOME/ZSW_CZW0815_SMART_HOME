##------------------------------------------
##--- Author: Pradeep Singh
##--- Blog: https://iotbytes.wordpress.com/programmatically-send-e-mail-from-raspberry-pi-using-python-and-gmail/
##--- Date: 21st Feb 2017
##--- Version: 1.0
##--- Python Ver: 2.7
##------------------------------------------



#import the class definition from "email_handler.py" file
from email_handler import Class_eMail

#set the email ID where you want to send the test email 
To_Email_ID = "zsw.projekt.test@gmail.com"

# warning
warning_subject = 'Warning!'
warning_text = 'Warning! \
                The password was incorrect. \
                Please enter the correct password.'

# Send Plain Text Email 
email = Class_eMail()
email.send_Text_Mail(To_Email_ID, warning_subject, warning_text)
del email
