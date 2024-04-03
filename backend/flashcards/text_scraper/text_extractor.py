import random
from text_reader import TextReader
from post_processing import PostProcessor

from ocr import OCR
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
           
    def extractParagraphs(self, filename):
        
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
    
    
    paragraph_data = textExtractor.extractParagraphs("TutorAI/backend/flashcards/text_scraper/assets/imageExample.pdf")
    for paragraph in paragraph_data:
        print("================================================")
        print(paragraph.text)
        print(paragraph.page_num)
        print(paragraph.pdf_name)
        print("\n\n")
    