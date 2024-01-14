import os
from pdfminer.high_level import extract_text

def convert_pdf_to_txt(pdf_file):
    """Convert a PDF file to text and return the path to the text file.
    
    Args:
        pdf_file (str/pdf): Path to the PDF file or the PDF file itself.
        
    Returns:
        str: Text content of PDF file.
    """
    # Extract text from the PDF file
    text = extract_text(pdf_file, codec='utf-8')
    return text
