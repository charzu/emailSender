# -*- coding: utf-8 -*-
import smtplib, imaplib, getpass, time
from email.mime.text import MIMEText

# with open(textfile, 'r') as f:
#   msg = MIMEText(f.read())


sender = 'charzu@vivaldi.net'  # the sender's email address
recipient = 'l.charzewski@gmail.com'  # the recipient's email address

msg = MIMEText("""Dzien dobry,
oto zawartosc maila.

dziekuje!
""")


msg['Subject'] = 'My First python email'
msg['From'] = sender
msg['To'] = recipient


s = smtplib.SMTP(host='smtp.vivaldi.net', port=587)
s.starttls()
s.login('charzu', 'tylko##do##testow')
s.sendmail(sender, [recipient], msg.as_string())
s.quit()



### On the IMAP connection, we need to move the mail in the "SENT" box
# you may need to be smarter there, since this name may change
sentbox_name = 'Sent'

im = imaplib.IMAP4_SSL(host='imap.vivaldi.net', port=993)

im.login('charzu', 'tylko##do##testow')
#M.login(getpass.getuser(), getpass.getpass())
print im.list()
# 1. Get the mail just sent in the INBOX
im.select('Sent', readonly=False)
im.append('Sent', r'UnMarked', imaplib.Time2Internaldate(time.time()) , msg.as_string())




