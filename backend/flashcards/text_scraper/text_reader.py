import fitz
from django.core.files.uploadedfile import InMemoryUploadedFile

from flashcards.learning_resources import Page


class TextReader:
    """
    A class for reading text from PDF files.
    """

    def read(self, file: InMemoryUploadedFile) -> list[Page]:
        """
        Reads text from the given PDF file.

        Args:
            pdf_file (str): The path to the PDF file.

        returns:
            list[Page]: a list of Page objects containing the text content of each page.

        Notes:
            This method extracts text from each page of the PDF file and stores it in the 'pages' list.
            It also extracts the name of the PDF file (without the .pdf extension) and stores it in 'bookname'.
        """
        file.seek(0)  # Ensure we're reading from the start of the file
        book_name: str = file.name

        # extract text from the PDF
        pages: list[Page] = []
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for index, current_page in enumerate(doc):
                page = Page(current_page.get_text(), index + 1, book_name)
                pages.append(page)
        return pages

    def read_page(self, file: InMemoryUploadedFile, page_number: int) -> str:
        """
        Reads text from a specific page of the given PDF file.

        Args:
            file (str): The path to the PDF file.
            page_number (int): The page number to read text from.

        Returns:
            str: The text content of the specified page.
        """
        if page_number >= self.get_amount_of_pages(file):
            # Page not in file
            raise ValueError("The file does not contain this page")

        file.seek(0)  # Ensure we're reading from the start of the file
        # extract text from the PDF
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for index, current_page in enumerate(doc):
                if index != page_number:
                    continue
                return current_page.get_text()

    def get_amount_of_pages(self, file: InMemoryUploadedFile) -> int:
        """get the amount of pages in a PDF file.

        Returns:
            int: the amput of pages.
        """

        file.seek(0)  # Ensure we're reading from the start of the file
        # extract text from the PDF
        pages = 0
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                pages += 1

        return pages
