import PyPDF2


class TextReader:

    def __init__(self) -> None:
        self.doc=[]

    def read(self,pdf_file):
        # Open the PDF file
        with open(pdf_file, 'rb') as f:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(f)
            
            self.doc=[]
            
            # Iterate through each page of the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Get the text from the current page
                page = pdf_reader.pages[page_num] 
                self.doc.append(page.extract_text())
    


        