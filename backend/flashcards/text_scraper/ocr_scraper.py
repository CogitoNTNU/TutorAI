
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import pytesseract
import numpy as np
from textblob import TextBlob
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_file = "TutorAI/backend/flashcards/text_scraper/assets/page_01.jpg"


#im: Image.Image = Image.open(image_file)
#im.show()
#im.save("TutorAI/backend/flashcards/text_scraper/assets/temp.png")



image = cv2.imread(image_file)
#cv2.imshow("Image", img)
cv2.waitKey(0)

text = pytesseract.image_to_string(image)
print(text)


#https://stackoverflow.com/questions/28816046/
#displaying-different-images-with-actual-size-in-matplotlib-subplot
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()



# not necessary for tessaract 4.0
def invert_image(image):
    inverted_img = cv2.bitwise_not(image)
    cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/inverted.jpg", inverted_img)


# binarization
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def binarize(image):
    gray_image = grayscale(image)
    thresh, im_bw = cv2.threshold(gray_image, 200, 230, cv2.THRESH_BINARY) # must calibrate these values
    return im_bw




# Noise Removal
def noise_removal(image):
    
    kernel = np.ones((1,1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1,1), np.uint8) # must calibrate these values
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

image = binarize(image)
no_noise = noise_removal(image)
cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/no_noise.jpg", no_noise)



# Dilation and Erosion

def thin_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image

def thick_font(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image



# Rotation and deskewing
# remove border before using this
#https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df
import numpy as np

def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage


def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)


new = cv2.imread("TutorAI/backend/flashcards/text_scraper/assets/page_01_rotated.jpg")

fixed = deskew(new)
cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/page_01_rotated_fixed.jpg", fixed)


# Remove boarders

def remove_borders(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_sorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    largest_bounding_box = contours_sorted[-1]
    x,y,w,h = cv2.boundingRect(largest_bounding_box)
    crop = image[y:y+h, x:x+w]
    return crop

crop = remove_borders(no_noise)
cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/no_noise_romeve_border.jpg", crop)



# Missing borders
def add_borders(image):
    color = [255, 255, 255]
    top, bottom, left, right = [150]*4
    image_with_border = cv2.copyMakeBorder(crop, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return image_with_border

image_with_border = add_borders(crop)
cv2.imwrite("TutorAI/backend/flashcards/text_scraper/assets/no_noise_romeve_border_with_border.jpg", image_with_border)







text = pytesseract.image_to_string(crop)


# Post processing
tb = TextBlob(text)
corrected = tb.correct()
# show the text after ocr-spellchecking has been applied
print("AFTER SPELLCHECK")
print("================")
print(corrected)
















