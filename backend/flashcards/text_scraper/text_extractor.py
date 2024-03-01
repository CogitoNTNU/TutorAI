from text_reader import TextReader


class TextExtractor:
    def __init__(self):
        self.pages=[]
        self.reader=TextReader()

    def extractTextPdf(self, filename):
        self.pages=self.reader.read(filename).pages



if __name__=="__main__":
    extr=TextExtractor()
    extr.extractTextPdf("Elise-Mohr-Skogan_Masteroppgave_V23_ferdig.pdf")