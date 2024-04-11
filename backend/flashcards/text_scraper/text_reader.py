import fitz
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
        print(f"Reading text from {file}", flush=True)
        text = ""
        file.seek(0)  # Ensure we're reading from the start of the file
        self.book_name = file.name
        # extract text from the PDF
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
                self.pages.append(text)

    def read_page(self, page_number: int) -> str:
        """
        Reads text from a specific page of the given PDF file.

        Args:
            file (str): The path to the PDF file.
            page_number (int): The page number to read text from.

        Returns:
            str: The text content of the specified page.

        Raises:
            FileNotFoundError: If the specified PDF file does not exist.
            ValueError: If the page number is out of range.
        """
        return self.pages[page_number - 1]
