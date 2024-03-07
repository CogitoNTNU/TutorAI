from text_reader import TextReader


class TextExtractor:
    def __init__(self):
        self.pages=[]
        self.reader=TextReader()

    def extractTextPdf(self, filename):
        self.reader.read(filename)
        self.pages=self.reader.pages
