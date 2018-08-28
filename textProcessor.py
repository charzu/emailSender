# -*- coding: utf-8 -*-
class ContentReader(object):
    template = None
    def __init__(self):
        object.__init__(self)
        self.subject = None
        self.content = None

    def readTemplate(self, filename):
        with open (filename) as stdin:
            self.template = stdin.read().split("\n")

    def buildContent(self, name, paper):
        self.subject = self.template[0]
        text = "\n".join(self.template[2:])
        self.content = text.format(name, paper)

    def printData(self):
        pass



if __name__ == '__main__':
    cr = ContentReader()
    cr.readTemplate("content.txt")
    cr.buildContent("NAME", "PAPER")

    print "SUBJECT:\n", cr.subject, "\n"
    print "CONTENT:\n", cr.content, "\n"
    #print len(cr.template)