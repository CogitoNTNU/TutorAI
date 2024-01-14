import os
import chardet

def convert_pdf_to_txt(pdf_file):
    """Convert a PDF file to text and return the path to the text file.
    
    Args:
        pdf_file (str/pdf): Path to the PDF file or the PDF file itself.
        
    Returns:
        str: Text content of PDF file.
    """
    # The pdf_file from the input is a django.core.files.uploadedfile.InMemoryUploadedFile.
    # Extract the text content of the file.

    file_content_bytes = pdf_file.read()
    encoding = chardet.detect(file_content_bytes)["encoding"]
    text = file_content_bytes.decode(encoding)

    return text
