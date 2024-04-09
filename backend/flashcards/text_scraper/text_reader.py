import PyPDF2
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


class TextReader:
    """
    A class for reading text from PDF files.

    Attributes:
        pages (list): A list to store text content extracted from each page of the PDF.
        bookname (str): Name of the PDF file being read.
    """

    def __init__(self) -> None:
        """
        Initializes the TextReader object with empty lists for pages and an empty string for bookname.
        """
        self.pages = []
        self.book_name = ""

    def __str__(self) -> str:
        """
        Returns a string representation of the TextReader object.

        Returns:
            str: A string containing the bookname followed by the text from all pages.
        """
        return f"{self.book_name}({' '.join(self.pages)})"

    def read(self, file: InMemoryUploadedFile):
        """
        Reads text from the given PDF file.

        Args:
            pdf_file (str): The path to the PDF file.

        Raises:
            FileNotFoundError: If the specified PDF file does not exist.

        Notes:
            This method extracts text from each page of the PDF file and stores it in the 'pages' list.
            It also extracts the name of the PDF file (without the .pdf extension) and stores it in 'bookname'.
        """
        # Open the PDF file
        byte_file = io.BytesIO(file)
        pdf_reader = PyPDF2.PdfReader(byte_file)

        self.pages = []

        # Iterate through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the text from the current page
            page = pdf_reader.pages[page_num]
            self.pages.append(page.extract_text())
            self.book_name = file.name

    def read_page(self, file, page_num):

        pdf_reader = PyPDF2.PdfReader(file)
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        return text
