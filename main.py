# -*- coding: utf-8 -*-
from auth import *
from msg import *
from msgFrame import *
from textProcessor import *
from xlsxProcessor import *


def _encode(var):
    if type(var) is 'unicode':
        return var.encode('utf-8')
    else:
        return var

def main():
    credentials = Authenticator("charzu", "1qaz2wsx")

    xp = XLSXprocessor("C:\Users\charzewski\Downloads\charzoApkaLista.xlsx")
    xp.openFile()
    cr = ContentReader()
    cr.readTemplate("content.txt")

    for row in xp:
        for cell in row:
            print type(cell.value)

        # data = [None for i in xrange(5)]
        # data[0] = row[0].value                           # gets cell values from the sheet # PUSTE JEST
        # data[1:5] =        [   cell.value.encode('utf-8') for cell in row[1:5]  ]   # first is a number
        # data[1:5] =        [   cell.value.encode('utf-8') for cell in row[1:5]  ]   # first is a number
        # data = [_encode(cell.value) for cell in row]
        data = [cell.value for cell in row]

        print data
        cr.buildContent(data[2], data[4])    # name, paper
        #if '+' in data[1]: continue    # don't send if already sanded

        con = cr.content
    #         con = """Dzien dobry,
    # oto zawartosc maila.
    #
    # dziekuje!
    # """

        # sub = "Temacik mejlunia!"
        # rec = 'l.charzewski@gmail.com'
        sub = cr.subject
        rec = data[3]  # e-mail address
        sen = 'charzu@vivaldi.net'
        mes = MsgBuilder(con, sub, rec, sen).build()

        # user check of the message
        window = MSGFrame(mes)
        window.show()
        # users decision
        if window.outcode == 'send':
            # proceed with sending
            print "decision: send"
            pass
        elif window.outcode == 'skip':
            print "decision: skip"
            # dont send, go to next entry from database
            continue
        elif window.outcode == 'abort':
            print "decision: abort"
            # stop looping, save changes end exit
            break

        hostSMTP = 'smtp.vivaldi.net'
        hostIMAP = 'imap.vivaldi.net'
        portSMTP = 587
        portIMAP = 993

        sentbox_name = 'Sent'


        sen = MsgSender(mes, hostSMTP, portSMTP,
                        credentials.username, credentials.password
                        )

        sen.send()
        # przechwycic jakis kod wyjscia z operacji wyslania
        # jesli nie wyjdzie to rzuca wyjatki.

        # print "KABOOOOOOM"
        row[1].value = '+'

        sav = MsgSaver(mes, hostIMAP, portIMAP,
                       credentials.username, credentials.password,
                       sentbox_name
                       )
        sav.save()

    #s =  smtplib.SMTP(host='smtp.vivaldi.net', port=587)

    xp.save()


if __name__ == '__main__':
    main()