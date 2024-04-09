import pytesseract
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

import pytesseract
import pypdfium2 as pdfium
from pypdfium2 import PdfPage

import flashcards.text_scraper.pipeline as piper


class OCR:
    def __init__(self, file: InMemoryUploadedFile):
        self.file: InMemoryUploadedFile = file
        self.image = None
        self.page_data = []

    def preprocess(self):
        """
        preprocesses the image without changing it's size or shape,
        returns the preprocessed image

        """
        chosen_pipeline = self.find_preprocessing_pipeine(self.image)
        pipeline: piper.Pipeline = piper.PipelineFactory(self.image).create_pipeline(
            chosen_pipeline
        )
        pipeline.apply_filters()
        return pipeline.get_image()

    def make_pdf_into_image_list(self, file: InMemoryUploadedFile) -> list[Image.Image]:
        """
        Converts a file into an image

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

    def find_preprocessing_pipeine(self, image):
        """
        Finds the preprocessing pipeline for the image
        """
        """
        TODO: Implement this function. For now, least viable product 
        """
        return 1

    def ocr_images(self, file: InMemoryUploadedFile):
        """
        take in pdf file, and calls a function that creates a list of images from the pdf file, then uses OCR to extract text from the images
        params: file: InMemoryUploadedFile
        """
        images: list[Image.Image] = self.make_pdf_into_image_list(file)

        for image in images:
            # TODO: self.preprocess()
            text = pytesseract.image_to_string(image)

            self.page_data.append(text)

    def ocr_page(self, pdf_file, page_num):
        """
        takes in a page, and uses OCR to extract text from the page
        params: page: PdfPage
        returns: text: str
        """
        page = pdfium.PdfDocument(pdf_file).get_page(page_num)

        image = page.render(scale=300 / 72).to_pil()
        # image = self.preprocess(image)
        text = pytesseract.image_to_string(image)
        return text

    def get_page_data(self):
        return self.page_data


if __name__ == "__main__":
    # pdf_file = "TutorAI/backend/flashcards/text_scraper/assets/example.pdf"

    # ocr = OCR(pdf_file)
    # ocr.ocr_images(pdf_file)
    # page_data = ocr.get_page_data()

    # for page in page_data:
    #     print(page)
    pass
