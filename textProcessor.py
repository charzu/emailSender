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

    def buildContent(self, name, paper):
        self.subject = self.template[0]
        text = "\n".join(self.template[2:])

        _name = name.encode('utf-8')  # convert to ascii
        _paper = paper.encode('utf-8')

        self.content = text.format(_name, _paper)


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
