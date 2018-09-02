# -*- coding: utf-8 -*-
from auth import *
from msg import *
from msgFrame import *
from textProcessor import *
from xlsxProcessor import *


def readConfig(file_path="config"):
    """
    reads program parameters
    :param file_path: path to config file to read
    :return: dictinary of parameters
    """
    with open(file_path, 'r') as stdin:
        parameters = {}
        for line in stdin:
            stripped_line = line.strip()
            if stripped_line:
                key = stripped_line.split()[0]
                val = " ".join(stripped_line.split()[1:])
                if val.isdigit():
                    val = int(val)
                parameters[key] = val
    return parameters


def main():
    # get parameters from file
    parameters = readConfig()

    credentials = Authenticator("charzu", "1qaz2wsx")
    # credentials = Authenticator()

    # xp = XLSXprocessor("C:\Users\charzewski\Downloads\charzoApkaLista.xlsx")
    # xp = XLSXprocessor("F:\Pobrane\charzoApkaLista.xlsx")
    xp = XLSXprocessor(parameters['xlsx_path'])
    xp.openFile()
    cr = ContentReader()
    cr.readTemplate(parameters['content_file'])

    for row in xp:
        data = [cell.value for cell in row]

        # print data
        cr.buildContent(data[2], data[4])  # name, paper

        # don't send if already sent
        if not data[1]:
            pass
        elif '+' in data[1]:
            continue

        con = cr.content
        sub = cr.subject
        rec = data[3]  # e-mail address
        sen = parameters['sender_address']
        mes = MsgBuilder(con, sub, rec, sen).build()

        # user check of the message
        window = MSGFrame(mes)
        window.show()

        # users decision
        if window.outcode == 'send':
            print "decision: send"
            # proceed with sending
            pass
        elif window.outcode == 'skip':
            print "decision: skip"
            # dont send, go to next entry from database
            continue
        elif window.outcode == 'abort':
            print "decision: abort"
            # stop looping, save changes end exit
            break

        sen = MsgSender(mes,
                        parameters['hostSMTP'], parameters['portSMTP'],
                        credentials.username, credentials.password
                        )

        sen.send()
        # if it fails an exception is thrown, and the program stops here
        # i believe that's good behaviour

        # mark entry as sent
        row[1].value = '+'

        # save updated version of excel file
        xp.save()
        # save the message in the inbox
        sav = MsgSaver(mes,
                       parameters['hostIMAP'], parameters['portIMAP'],
                       credentials.username, credentials.password,
                       parameters['sentbox_name']
                       )
        sav.save()


if __name__ == '__main__':
    main()
