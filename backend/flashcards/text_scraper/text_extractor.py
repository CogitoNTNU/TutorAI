from text_reader import TextReader


class TextExtractor:
    def __init__(self):
        self.pages=[]
        self.reader=TextReader()

    def extractTextPdf(self, filename):
        self.reader.read(filename)
        self.pages=self.reader.pages




if __name__=="__main__":
    extr=TextExtractor()
    extr.extractTextPdf("assets/book-riscv-rev1.pdf")
    for page in extr.pages:
        print(page)
    print(extr.reader.bookname)
