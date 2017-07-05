class News:
    def __init__(self):
        self.title = ''
        self.content = ''
        self.imageUrl = ''
        self.referenceUrl = ''

    def setData(self, title, content, imageUrl, referenceUrl):
        self.title = title
        self.content = content
        self.imageUrl = imageUrl
        self.referenceUrl = referenceUrl

    def getData(self):
        return {'title': self.title, 'content': self.content, 'image': self.imageUrl, 'reference': self.referenceUrl}

