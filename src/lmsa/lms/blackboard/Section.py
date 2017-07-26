class Section(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
