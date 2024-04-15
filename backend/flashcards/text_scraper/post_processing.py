""" This is the post-processing module for the text scraper. It contains a class that performs post-processing on the extracted text data. The post-processing class is responsible for cleaning up the extracted text data and extracting paragraphs from the page content. The extracted paragraphs are then stored in a data class object for further processing."""

from dataclasses import dataclass


@dataclass
class Page:
    text: str
    page_num: int
    pdf_name: str


class PostProcessor:

    def __init__(self):
        pass

    def page_post_processing(self, page_data, pdf_name):
        data = []

        for i, page in enumerate(page_data):
            paragraphs = self.extract_paragraphs(page)

            for paragraph in paragraphs:
                page_num = i + 1
                data.append(Page(text=paragraph, page_num=page_num, pdf_name=pdf_name))

        return data

    def extract_paragraphs(self, page):
        """
        Extract paragraphs from a list of strings, where each string represents page content from a PDF.

        Parameters:
        - page_data: list of strings, where each string represents the content of a page.

        Returns:
        - A list of paragraphs extracted from the page content.
        """
        paragraphs = []

        # Split the page into segments based on double newline characters
        segments = page.split("\n\n")

        # Further process each segment
        # for segment in segments:
        #     # Clean up the segment by stripping leading/trailing whitespace and replacing multiple newlines with a single space
        #     cleaned_segment = ' '.join(segment.strip().split('\n'))
        #     cleaned_segment = self.simple_clean(cleaned_segment)

        #     # Ignore empty segments
        cleaned_segment = self.simple_clean(page)
        paragraphs.append(cleaned_segment)

        return paragraphs

    def simple_clean(self, text, replace_with="?"):

        return "".join(char if ord(char) < 255 else replace_with for char in text)
