# -*- coding: utf-8 -*-
from Tkinter import *


class Authenticator(object):
    def __init__(self, u="", p=""):
        super(Authenticator, self).__init__()
        self.username = u
        self.password = p
        if not all((self.username, self.password)):
            self.getCredentials()

    def getCredentials(self):
        def onpwdentry(evt):
             self.username = usrnbox.get()
             self.password = pwdbox.get()
             root.destroy()

        def onokclick():
             self.username = usrnbox.get()
             self.password = pwdbox.get()
             root.destroy()

        root = Tk()
        fr = Frame(root)
        fr.pack()

        usrnbox = Entry(fr)
        pwdbox  = Entry(fr, show = '*')

        Label(fr, text = 'Username: ').grid(row = 0, column=0)
        usrnbox.grid(row=0, column=1)
        Label(fr, text = 'Password: ').grid(row=1, column=0)
        pwdbox. grid(row=1, column=1)

        pwdbox.bind('<Return>', onpwdentry)
        Button(root, command=onokclick, text = 'OK').pack(side = 'top')

        root.mainloop()


if __name__ == '__main__':
    p = Authenticator()
    print p.username
    print p.password

