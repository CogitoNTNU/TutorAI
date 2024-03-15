import random
from text_reader import TextReader

from ocr import OCR
import PyPDF2
from django.core.files.uploadedfile import InMemoryUploadedFile



class TextExtractor:
    def __init__(self):
        self.pages=[]
        self.reader=TextReader()

    def extractTextPdf(self, filename):
        self.reader.read(filename)
        self.pages=self.reader.pages
        
    def extractTextImage(self, filename):
        
        ocr: OCR = OCR(filename)
        ocr.ocr_images(filename)
        page_data = ocr.get_page_data()
        return page_data
    
    def isReadable(self, filename) -> bool:
        
        
        file = open(filename, 'rb')

        pdf_reader = PyPDF2.PdfFileReader(file)
        total_pages1 = pdf_reader.numPages
        
        pages = []
        for i in range(3): # TODO: change to 3 woth log2(total_pages1)
            page_number = random.randint(0, total_pages1 - 1)
            try:
                pages.append(pdf_reader.getPage(page_number))
            except Exception:
                print("not enough pages")
                continue
        
        text = ""
        ocr_text = ""
        for page in pages:
            text += page.extractText() #TODO make correct functions to extract text
            ocr = OCR(filename)
            ocr_text += ocr.ocr_page(page)
            
        if len(text) / len(ocr_text) > 0.88:
            return True
        return False
            
        

    def _pdf_readable(file: InMemoryUploadedFile) -> bool:
        """
        Checks if a PDF file is easily readable by attempting to extract text directly from it.

        This method does not guarantee OCR accuracy but checks if the PDF contains selectable text,
        which is a good indicator of the document's readability without needing image conversion.

        Args:
            file: The PDF file to check, wrapped in a Django InMemoryUploadedFile object.

        Returns:
            True if the file is easily readable (contains a significant amount of selectable text),
            False otherwise.
        """
        try:
            # Open the PDF file directly from the InMemoryUploadedFile
            with fitz.open(stream=file.read(), filetype="pdf") as doc:
                text_length = 0
                # Iterate through each page and attempt to extract text
                for page in doc:
                    text = page.get_text()
                    text_length += len(text)

                # Consider the PDF easily readable if we extracted a significant amount of text
                # Adjust the threshold according to your needs
                return text_length > 100  # Example threshold
        except Exception as e:
            # If an error occurred, we use ocr
            return False
           
        
        
        
    
    


if __name__=="__main__":
    # extr=TextExtractor()
    # extr.extractTextPdf("assets/book-riscv-rev1.pdf")
    # for page in extr.pages:
    #     print(page)
    # print(extr.reader.bookname)
    
    print(TextExtractor._pdf_readable("TutorAI/backend/flashcards/text_scraper/assets/example.pdf"))
