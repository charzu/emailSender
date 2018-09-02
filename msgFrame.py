# -*- coding: utf-8 -*-
from Tkinter import *
from email.mime.text import MIMEText
import re, os


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def cleanempty(text):
    return os.linesep.join([s for s in text.splitlines() if s])


def clean(text):
    return cleanempty(cleanhtml(text))

class MSGFrame(object):
    def __init__(self, msg):
        self.msg = msg
        self.outcode = None

    def show(self):
        def onsendclick():
            self.outcode = "send"
            root.destroy()

        def onskipclick():
            self.outcode = "skip"
            root.destroy()

        def onabortclick():
            self.outcode = "abort"
            root.destroy()

        root = Tk()
        fr = Frame(root)
        fr.pack()

        mes = Text(fr)
        mes.insert(INSERT, clean(self.msg.as_string()))
        mes.grid(row=1, column=1)

        fr1 = Frame(fr)
        fr1.grid(row=2, column=1)
        b1 = Button(fr1, command=onsendclick, text='Send')
        b1.grid(row=1, column=1)
        b2 = Button(fr1, command=onskipclick, text='Skip')
        b2.grid(row=1, column=2)
        b3 = Button(fr1, command=onabortclick, text='Abort')
        b3.grid(row=1, column=3)

        root.mainloop()


if __name__ == '__main__':
    text = """Ala
    ma
    
    kotka!"""

    msg = MIMEText(text)
    msg['To'] = "ktos@gdzies.pl"
    msg['From'] = "ja@tu.pl"
    msg['Subject'] = "Oto temat!"

    a = MSGFrame(msg)
    a.show()
    print "koniec programu"
