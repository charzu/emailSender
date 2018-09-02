# -*- coding: utf-8 -*-
import imaplib
import smtplib
import time
from email.mime.text import MIMEText


class MsgBuilder(object):
    def __init__(self, content, subject, recipient, sender):
        super(MsgBuilder, self).__init__()
        self.content = content
        self.subject = subject
        self.recipient = recipient
        self.sender = sender

    def build(self):
        msg = MIMEText(self.content)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        return msg


class MsgSender(object):
    def __init__(self, msg, host, port, username, password):
        super(MsgSender, self).__init__()
        self.msg = msg
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send(self):
        ## czy mozna otworzyc SMTP w init'cie?
        ## gdzie wtedy zamykac polaczenie?
        # s = smtplib.SMTP(host='smtp.vivaldi.net', port=587)
        s = smtplib.SMTP(host=self.host, port=self.port)
        s.starttls()

        # haslo trzeba pobrac od uzytkownika - lib: getpass
        s.login(self.username, self.password)
        # s.sendmail(sender, [recipient], msg.as_string())
        s.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())
        a = s.quit()
        # print a

class MsgSaver(object):
    def __init__(self, msg, host, port, username, password, sentbox_name):
        super(MsgSaver, self).__init__()
        self.msg = msg
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.sentbox_name = sentbox_name

    def save(self):
        ### On the IMAP connection, we need to move the mail in the "SENT" box
        # you may need to be smarter there, since this name may change
        im = imaplib.IMAP4_SSL(host=self.host, port=self.port)

        im.login(self.username, self.password)

        # a way to find SentBox name on a server:
        # print im.list()

        # 1. Get the mail just sent in the INBOX
        im.select(self.sentbox_name, readonly=False)
        im.append(self.sentbox_name,
                  r'UnMarked',
                  imaplib.Time2Internaldate(time.time()),
                  self.msg.as_string()
                  )
        im.logout()



