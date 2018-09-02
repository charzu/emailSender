# -*- coding: utf-8 -*-


class ContentReader(object):
    template = None

    def __init__(self):
        object.__init__(self)
        self.subject = None
        self.content = None

    def readTemplate(self, filename):
        with open(filename) as stdin:
            self.template = stdin.read().split("\n")

    # def buildContent(self, name, paper):
    #     self.subject = self.template[0].decode('utf-8')
    #     text = u"\n".join(self.template[2:]).decode('utf-8')   # .encode('utf-8')
    #     self.content = text.format(name.decode('utf-8'),
    #                                paper.decode('utf-8')
    #                                )

    def buildContent(self, name, paper):
        self.subject = self.template[0]
        text = "\n".join(self.template[2:])  # .encode('utf-8')
        print type(text)

        _name = name.encode('utf-8')
        _paper = paper.encode('utf-8')

        self.content = text.format(_name,
                                   _paper
                                   )

    def printData(self):
        pass


if __name__ == '__main__':
    print type("aąbć")
    cr = ContentReader()
    cr.readTemplate("content.txt")
    # print cr.template
    # a = " ".join(cr.template[2:])

    cr.buildContent(u"NAMEŁ",
                    u"PAPERĄ"
                    )

    print "SUBJECT:\n", cr.subject, "\n"
    print "CONTENT:\n", cr.content, "\n"
    # print len(cr.template)
