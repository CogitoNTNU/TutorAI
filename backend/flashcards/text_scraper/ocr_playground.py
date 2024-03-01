
import pytesseract
from PIL import Image
import im_processing_playground as imP 

img_file = "TutorAI/backend/flashcards/text_scraper/assets/page_01.jpg"

no_noise = imP.noise_removal(img_file)

img: Image.Image = Image.open(img_file)

ocr_result = pytesseract.image_to_string(img_file)
print(no_noise)