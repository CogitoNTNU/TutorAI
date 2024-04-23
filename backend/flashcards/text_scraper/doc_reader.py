import os
from docx import Document
from post_processing import Page, PostProcessor
from django.core.files.uploadedfile import InMemoryUploadedFile
import win32com.client as win32


class DocReader:

    def get_text_from_docx(self, file: InMemoryUploadedFile):
        """Extract text from a DOCX file."""
        print("Extracting text from DOCX file")
        document = Document(file)
        pages: list[Page] = []
        for i, para in enumerate(document.paragraphs):
            pages.append(Page(text=para.text, page_num=i, pdf_name=os.path.basename(file)))
        
        return pages

    def get_text_from_doc(self, file: InMemoryUploadedFile):
        """Extract text from a DOC file using COM automation."""
        print("Extracting text from DOC file")
        if not  file.name.endswith('.docx'):
            return "This file is not a valid doc file."
        post_processor = PostProcessor()
        word = win32.Dispatch("Word.Application")
        word.visible = False
        pages: list[Page] = []
        try:
            doc = word.Documents(file)
            for i, para in enumerate(doc.Paragraphs):
                pages.append(Page(text=para.Range.Text, page_num=i, pdf_name=os.path.basename(file)))
          
            doc.Close()
            post_processor.page_post_processing(pages)
        finally:
            word.Quit()
        return pages
    
    def extract_text_from_docx(uploaded_file: InMemoryUploadedFile):
    # Ensure the file is a .docx
        pages : list[Page] = []
        if uploaded_file.name.endswith('.docx'):
            # Load the document
            document = Document(uploaded_file)

            # Extract text from the document pages, adding them to page
            for i, para in enumerate(document.paragraphs):
                pages.append(Page(text=para.text, page_num=i, pdf_name=os.path.basename(uploaded_file)))
            return pages
            text = '\n'.join([paragraph.text for paragraph in document.paragraphs])

        else:
            return "This file is not a valid docx file."

    def get_text_from_doc_or_docx(self, file: InMemoryUploadedFile):
        """Determine the file type and extract text accordingly."""
        print("Extracting text from DOC or DOCX file")
        post_processor = PostProcessor()
        _, file_extension = os.path.splitext(file)
        if file_extension.lower() == '.docx':
            processed_pages = post_processor.page_post_processing(self.get_text_from_docx(file))
            return processed_pages
        elif file_extension.lower() == '.doc':
            processed_pages = post_processor.page_post_processing(self.get_text_from_doc(file))
            return processed_pages
        else:
            raise ValueError("Unsupported file type")

