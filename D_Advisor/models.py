class algorithm_ml:
    def __init__(self, title=None, date=None, content=None ):
        self.title = title
        self.content = content
        self.date = date

    def setTitle(self, title):
        self.title = title
    def setDate(self, date):
        self.date = date
    def setContent(self, content):
        self.content = content

    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getContent(self):
        return self.content