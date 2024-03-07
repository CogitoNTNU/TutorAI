

from spire.pdf.common import *
from spire.pdf import *
import pytesseract
import io
from PIL import Image

import pipeline as piper


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




class OCR:
    def __init__(self, file):
        self.file = file
        self.image = None
        self.page_data = []
        
    def hoppelopp(self):
        """
        loops through each page of the pdf and extracts the text
        """
        
        # Create a PdfDocument object
        doc = PdfDocument()

        # Load a PDF document
        doc.LoadFromFile(self.file)

        # Get a specific page
        for page_num in range(doc.Pages.Count):
            page = doc.Pages[page_num]
            try:
                # Extract image from the page
                images = page.ExtractImages()
                if images:
                    self.image = Image.open(io.BytesIO(images[0]))
                    self.preprocess()
                    text = self.get_text()
                    self.page_data.append(text)
                else:
                    print(f"No images found on page {page_num}")
            except SpireException as e:
                print(f"An error occurred while extracting images from page {page_num}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        doc.Close()
            
            
        
    def preprocess(self):
        """
        preprocesses the image
        """
        pipeline: piper.Pipeline = piper.PipelineFactory(self.image).create_pipeline(1)
        pipeline.pipe()
        self.image = pipeline.get_image()

    def get_text(self):
        """
        get text from pytesseract
        """
        text =  pytesseract.image_to_string(self.image)
        return text
    
    def get_page_data(self):
        return self.page_data
        
    
if __name__=="__main__":
    pdf_file = "TutorAI/backend/flashcards/text_scraper/assets/imageExample.pdf"
    
    ocr = OCR(pdf_file)
    ocr.hoppelopp()
    ocr.get_page_data()
    
    for page in ocr.page_data:
        print(page)
