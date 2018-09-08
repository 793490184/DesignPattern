class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog=u'小狗', cat=u'小猫')

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()

e, g = get_localizer("English"), get_localizer("China")
for msgid in 'Dog parrot cat bear dog'.split():
    print(e.get(msgid), g.get(msgid))
