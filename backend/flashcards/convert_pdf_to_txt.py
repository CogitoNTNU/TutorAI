import os
from pdfminer.high_level import extract_text

def convert_pdf_to_txt(pdf_file_path):
    """Convert a PDF file to text and return the path to the text file."""
    # Extract text from the PDF file
    text = extract_text(pdf_file_path, codec='utf-8')
    # Create a text file in the same directory as the PDF file
    txt_file_path = os.path.splitext(pdf_file_path)[0] + '.txt'
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        # Write the text to the text file
        txt_file.write(text)
    return txt_file_path

# TODO remove: Test the function. The PDF file should be in the same directory as this file. Path: backend/flashcards/test.pdf
if __name__ == '__main__':
    pdf_file_path = os.path.join(os.path.dirname(__file__), 'test.pdf')
    txt_file_path = convert_pdf_to_txt(pdf_file_path)
    print(txt_file_path)
