#email_delete.py

# Project 1 - delete gmail spam

import imaplib
import email
from email.header import decode_header

username = 'erk991122@gmail.com'
password = 'awesome991122'

imap = imaplib.IMAP4_SSL("imap.gmail.com")

imap.login(username, password)


imap.select('INBOX')
#search for specific mail by sender
status, messages = imap.search(None, 'FROM "contact@campaigns.rnchq.com"')

messages = messages[0].split(b' ')

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            #decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                #if bytes type, decode to str
                subject = subject.decode()
            print("Deleting", subject)
        #mark mail as deleted
        imap.store(mail, "+FLAGS", "\\Deleted")


imap.expunge()

imap.close()

imap.logout()
