from PIL import Image
from matplotlib import pyplot as plt
import cv2
import pytesseract
import numpy as np
from textblob import TextBlob
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ImageProcessing:



def invert_image(image):
    inverted_img = cv2.bitwise_not(image)
    cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/inverted.jpg", inverted_img)



