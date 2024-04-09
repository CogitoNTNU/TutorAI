import random
from flashcards.text_scraper.text_reader import TextReader
from flashcards.text_scraper.post_processing import Data, PostProcessor

from flashcards.text_scraper.ocr import OCR
import PyPDF2
from django.core.files.uploadedfile import InMemoryUploadedFile



class TextExtractor:
    def __init__(self):
        self.pages=[]
        self.reader=TextReader()
        self.post_processor = PostProcessor()
        
    def extractText(self, filename):
        if self.is_readable(filename):
            self.extractTextPdf(filename)
        else:
            self.extractTextImage(filename)
        

    def extractTextPdf(self, filename):
        self.reader.read(filename)
        self.pages=self.reader.pages
        
        
    def extractTextImage(self, filename):
        
        ocr: OCR = OCR(filename)
        ocr.ocr_images(filename)
        page_data = ocr.get_page_data()
        self.pages = page_data
    
    def is_readable(self, filename) -> bool:
        
        """
        Checks if a PDF file is easily readable by attempting to extract text directly from it.

        This method does not guarantee OCR accuracy but checks if the PDF contains selectable text,
        which is a good indicator of the document's readability without needing image conversion.

        Args:
            file: The PDF file to check.

        Returns:
            True if the file is easily readable (contains a significant amount of selectable text),
            False otherwise.
        """
        
        self.reader.read(filename)
        total_pages1 = len(self.reader.pages) 
        
        text = ""
        ocr_text = ""
        ocr = OCR(filename)
        
        for i in range(3): # TODO: change to 3 with log2(total_pages1)
            page_number = random.randint(0, total_pages1 - 1)
                       
            text += self.reader.read_page(filename, page_number)
            ocr_text += ocr.ocr_page(filename, page_number)
            
                
            
        if len(ocr_text) == 0: return True #TODO: lag feilmelding
        if len(text) / len(ocr_text) > 0.88:
            return True
        return False
            
        

    
           
    def extractParagraphs(self, filename) -> list[Data]:
        
        """Entry point for the text extraction process. This method extracts text from a PDF file and performs post-processing on the extracted text data.

        Returns:
            @dataclass
            class Data:
                text: str
                page_num: int
                pdf_name: str
        """
        
        self.extractText(filename)
        pdf_name = filename[:filename.find(".pdf")]
        
        data = self.post_processor.page_post_processing(self.pages, pdf_name)
        return data
     


        
        
        
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
        # Here, you could add any post-processing to clean up the text
    return text




if __name__=="__main__":
    #extr=TextExtractor()
    #extr.extractTextPdf("TutorAI/backend/flashcards/text_scraper/assets/imageExample.pdf")
    
    textExtractor = TextExtractor()
    
    #page_data = textExtractor.extractText("TutorAI/backend/flashcards/text_scraper/assets/imageExample.pdf")
    
    
    paragraph_data = textExtractor.extractParagraphs("TutorAI/backend/flashcards/text_scraper/assets/example.pdf")
    for paragraph in paragraph_data:
        print("================================================")
        print(paragraph.text)
        print(paragraph.page_num)
        print(paragraph.pdf_name)
        print("\n\n")
    