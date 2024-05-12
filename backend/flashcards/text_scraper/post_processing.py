""" This is the post-processing module for the text scraper. It contains a class that performs post-processing on the extracted text data. The post-processing class is responsible for cleaning up the extracted text data and extracting paragraphs from the page content. The extracted paragraphs are then stored in a data class object for further processing."""

from flashcards.learning_resources import Page


class PostProcessor:

    def page_post_processing(self, pages: list[Page]) -> list[Page]:
        """Post processes the extracted text data.

        Args:
            pages (list[Page]): pages to be processed

        Returns:
            list[Page]: processed pages
        """
        post_processed_pages = []

        for index, page in enumerate(pages):
            prev_sentence = self.get_last_sentence_in_previous_page(index, pages)
            next_sentence = self.get_first_sentence_in_next_page(index, pages)
            
            # TODO: Add functionality here to guess the page number of current page
            post_processed_pages.append(
                self._extract_paragraphs(page, prev_sentence, next_sentence)
            )

        return post_processed_pages

    def get_last_sentence_in_previous_page(self, page_num, pages) -> str:
        """gets the last sentence in the previous page of the PDF.

        Args:
            page_num
            pages

        Returns:
            str: the last sentence in the previous page of the PDF.
        """
        if page_num == 0:
            return ""

        page_text = pages[page_num - 1].text
        last_period_index = page_text.rfind(".")
        return page_text[last_period_index + 1 :].strip()

    def get_first_sentence_in_next_page(self, page_num, pages) -> str:
        """Gets the first sentence in the next page of the PDF.

        Args:
            page_num (_type_):
            pages (_type_):

        Returns:
            _type_: string
        """

        if page_num == len(pages) - 1:
            return ""

        page_text = pages[page_num + 1].text
        first_period_index = page_text.find(".")

        if first_period_index == -1:
            return page_text
        else:
            return page_text[:first_period_index].strip()

    def _extract_paragraphs(
        self, page: Page, prev_sentence: str, next_sentence: str
    ) -> Page:
        """
        Extract paragraphs from a list of strings, where each string represents page content from a PDF.

        Parameters:
        - page_data: list of strings, where each string represents the content of a page.

        Returns:
        - A list of paragraphs extracted from the page content.
        """

        page.text = (str)(prev_sentence + page.text + next_sentence)
        cleaned_segment = self._simple_clean(page.text)
        page.text = cleaned_segment

        return page

    def _simple_clean(self, text, replace_with="�") -> str:
        """cleans the text by replacing characters with ord > 255 with a specified character.

        Args:
            text (_type_): _description_
            replace_with (str, optional): _description_. Defaults to "?".

        Returns:
            str: _description_
        """

        return "".join(char if ord(char) < 255 else replace_with for char in text)
