""" This is the post-processing module for the text scraper. It contains a class that performs post-processing on the extracted text data. The post-processing class is responsible for cleaning up the extracted text data and extracting paragraphs from the page content. The extracted paragraphs are then stored in a data class object for further processing."""

from dataclasses import dataclass


@dataclass
class Page:
    text: str
    page_num: int
    pdf_name: str


class PostProcessor:

    def page_post_processing(self, pages: list[Page]) -> list[Page]:
        post_processed_pages = []

        for index, page in enumerate(pages):
            prev_sentence = self.get_last_sentence_in_previous_page(index, pages)
            next_sentence = self.get_first_sentence_in_next_page(index, pages)
            post_processed_pages.append(self._extract_paragraphs(page, prev_sentence, next_sentence))

        return post_processed_pages
    
    def get_last_sentence_in_previous_page(self, page_num, pages):
        if page_num == 0:
            return ""
        page =  pages[page_num - 1]
        text = page.text.split(".")
        return text[-1]
    
    def get_first_sentence_in_next_page(self, page_num, pages):
        if page_num == len(pages) - 1:
            return ""
        page =  pages[page_num + 1]
        text = page.text.split(".")
        return text[0]
    
    

    def _extract_paragraphs(self, page: Page, prev_sentence: str, next_sentence: str) -> Page:
        """
        Extract paragraphs from a list of strings, where each string represents page content from a PDF.

        Parameters:
        - page_data: list of strings, where each string represents the content of a page.

        Returns:
        - A list of paragraphs extracted from the page content.
        """

        # Split the page into segments based on double newline characters
        # segments = page.split("\n\n")

        # Further process each segment
        # for segment in segments:
        #     # Clean up the segment by stripping leading/trailing whitespace and replacing multiple newlines with a single space
        #     cleaned_segment = ' '.join(segment.strip().split('\n'))
        #     cleaned_segment = self.simple_clean(cleaned_segment)

        #     # Ignore empty segments

        page.text = (str)(prev_sentence + page.text + next_sentence)
        cleaned_segment = self._simple_clean(page.text)
        page.text = cleaned_segment

        return page

    def _simple_clean(self, text, replace_with="?"):

        return "".join(char if ord(char) < 255 else replace_with for char in text)
