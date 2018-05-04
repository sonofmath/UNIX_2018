#!/usr/bin/python
#encoding:utf-8
 
import os, sys, time, argparse, subprocess

import email
from imapclient import IMAPClient

HOSTNAME = 'imap.gmail.com'
USERNAME = 'jrsraspberrypi@gmail.com'
PASSWORD = 'RaspPi3.14'
MESSAGE_SUBJECT = 'Contact form submitted'

MAILBOX = 'Inbox'
TARGET = '/home/pi/'  # this is the path where attachments are stored 
CHECK_FREQ = 30 # in seconds

def parse_arguments(sysargs):
    """ Setup the command line options. """

    description = '''The script parseIMAPemail.py is looped and repeatedly 
    checks a mail box if a mail with a specified subject has arrived.
    If so, the emails attachment is stored. This script is a part of the tutorial 
    www.knight-of-pi.org/accessing-and-parsing-emails-with-the-raspberry-pi-and-imapclient'''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--username', nargs='?', metavar='str', type=str,
                                    default=USERNAME, help='Username of the Email account',)
    parser.add_argument('-s', '--subject', nargs='?', metavar='str', type=str,
                                     default=MESSAGE_SUBJECT, help='The subject new emails should be scanned for')
    parser.add_argument('--host', nargs='?', metavar='str', type=str,
                                     default=HOSTNAME, help='Name of the IMAP host webserver')
    parser.add_argument('--pwd', nargs='?', metavar='str', type=str,
                                     default=PASSWORD, help='Password belonging to the username')

    return parser.parse_args(sysargs)




def scan_emails(args, unread):
    """ Scan all unread Emails for the given Subject. """

    for msg_id, stuff in unread.iteritems():
        new_email = email.message_from_string(unread[msg_id]['RFC822'])
        
        if new_email['subject'] == args.subject:
            print "Found subject! Running pump!",  msg_id
	    # Runs shell script that activates the pump
	    #subprocess.call(['./home/pi/Desktop/UNIXPROJECT/runpump.sh'])
	    os.system('sh /home/pi/Desktop/UNIXPROJECT/runpump.sh')
            

def loop(args):
    """ Main loop: log into the IMAP server and fetch all unread emails,
         which are delegated into scan_emails. """

    print('Logging into ' + args.username)

    server = IMAPClient(args.host, use_uid=True, ssl=True)
    server.login(args.username, args.pwd)   
    
    select_info = server.select_folder(MAILBOX)
    messages = server.search(['UNSEEN'])
    all_unread = server.fetch(messages, ['RFC822'])
    scan_emails(args, all_unread)

    #time.sleep(CHECK_FREQ)


 
if __name__ == '__main__':
    args = parse_arguments(sys.argv[1:])

    #try:
        #while True:
    loop(args)
    #finally:
        #pass