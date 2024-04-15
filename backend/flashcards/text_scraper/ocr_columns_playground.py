import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image_file = "TutorAI/backend/flashcards/text_scraper/assets/page_01_rotated.jpg"


image: Image.Image = Image.open(image_file)

ocr_result = pytesseract.image_to_string(image)
print(ocr_result)
