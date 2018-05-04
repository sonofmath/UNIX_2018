#!/usr/bin/python
import os, re
import sys
import smtplib

#from email.mime.image import MIMEImage
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


sender = 'jrsraspberrypi@gmail.com'
password = "RaspPi3.14"
recipient = sys.argv[1]
subject = ''
message = sys.argv[3]
BODY_HTML = '<!DOCTYPE html><html><head><title>TEST</title></head><body><h1><b>Click Button Link to Run Pump!</b></h1><br/><a href="org.coloradomesa.edu/~jemathson/index.html"><img src="https://cdn.dribbble.com/users/60701/screenshots/471795/btn_orange_dribbble.png"></a></body></html>'

def main():
    print("I am running the py script!")
    msg = MIMEMultipart()
    msg['Subject'] = sys.argv[2]
    msg['To'] = recipient
    msg['From'] = sender

    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    msg.attach(MIMEText(BODY_HTML, 'html'))

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo

    session.login(sender, password)

    #fp = open(sys.argv[3], 'rb')
    #msgq = MIMEBase('audio', 'audio')
    #msgq.set_payload(fp.read())
    #fp.close()
    # Encode the payload using Base64
    #encoders.encode_base64(msgq)
    # Set the filename parameter
    #filename=sys.argv[4]
    #msgq.add_header('Content-Disposition', 'attachment', filename=filename)
    #msg.attach(msgq)
    # Now send or store the message
    qwertyuiop = msg.as_string()



    session.sendmail(sender, recipient, qwertyuiop)

    session.quit()
    #os.system('notify-send "Email sent"')

if __name__ == '__main__':
    main()
