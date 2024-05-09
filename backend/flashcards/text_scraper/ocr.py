from multiprocessing import pool
import pytesseract
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.learning_resources import Page
import pytesseract
import pypdfium2 as pdfium
from pypdfium2 import PdfPage

from flashcards.text_scraper.pipeline import create_pipeline, Pipeline


class OCR:
    def __init__(self, file: InMemoryUploadedFile):
        self.file: InMemoryUploadedFile = file
        self.image = None
        self.page_data: list[Page] = []

    def preprocess(self):
        """
        preprocesses the image without changing it's size or shape,
        returns the preprocessed image

        returns:
            Image: the preprocessed image
        """
        pipeline: Pipeline = create_pipeline(self.image)
        return pipeline.apply_filters()

    def make_pdf_into_image_list(self, file: InMemoryUploadedFile) -> list[Image.Image]:
        """
        Converts a file into an image. The file can be in any format that can be converted into an image.

        Args:
            file: The file to convert into an image
        Returns:
            List of image names for the given files' pages
        """

        pdf = pdfium.PdfDocument(file)

        n_pages = len(pdf)
        pages_as_images = []
        for page_number in range(n_pages):
            page: PdfPage = pdf.get_page(page_number)
            pil_image = page.render(
                scale=300 / 72
            ).to_pil()  # Probably possible to optimize this.
            image_name = f"page_{page_number}"
            image_name = f"{image_name}.jpg"

            pages_as_images.append(pil_image)
        return pages_as_images

    def make_pillow_image(self, file: InMemoryUploadedFile) -> list[Image.Image]:
        """
        Converts a file into an image. The file can be in any format that can be converted into an image.

        Args:
            file: The file to convert into an image
        """
        images: list[Image.Image] = []
        for chunk in file.chunks():
            image = Image.open(file)
            images.append(image)
        return images

    def ocr_images(self, file: InMemoryUploadedFile):
        """
        take in pdf file, and calls a function that creates a list of images from the pdf file, then uses OCR to extract text from the images
        params: file: InMemoryUploadedFile
        """
        if file.name.endswith(".pdf"):
            images: list[Image.Image] = self.make_pdf_into_image_list(file)
        else:
            images: list[Image.Image] = self.make_pillow_image(file)
        print("number of images: ", len(images), flush=True)
        for index, image in enumerate(images):
            # TODO: self.preprocess()
            print("OCR-ing image-------------------------------------")
            text = pytesseract.image_to_string(image)
            page = Page(text, index + 1, file.name)
            self.page_data.append(page)
            print(page.text)

    def ocr_page(self, pdf_file, page_num) -> str:
        """
        takes in a page, and uses OCR to extract text from the page
        params: page: PdfPage
        returns: text: str
        """
        page = pdfium.PdfDocument(pdf_file).get_page(page_num)

        image = page.render(scale=300 / 72).to_pil()
        # TODO: add functionality for preprocessing
        # image = self.preprocess(image)
        text: str = pytesseract.image_to_string(image)
        return text

    def get_page_data(self):
        return self.page_data
