from PIL import Image
from matplotlib import pyplot as plt
import cv2
import pytesseract
import numpy as np
from textblob import TextBlob
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ImageProcessor:
    
    def __init__(self, image):
        self.image = image

    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image

    def invert_image(self):
        self.image = cv2.bitwise_not(self.image)
        
    def grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def binarize(self):
        gray_image = self.grayscale(self.image)
        thresh, im_bw = cv2.threshold(gray_image, 200, 230, cv2.THRESH_BINARY) # must calibrate these values
        self.image =  im_bw
    
    def noise_removal(self):
        kernel = np.ones((1,1), np.uint8)
        image = cv2.dilate(self.image, kernel, iterations=1)
        kernel = np.ones((1,1), np.uint8) # must calibrate these values
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 3)
        self.image = image

    def thin_font(self):
        image = cv2.bitwise_not(self.image)
        kernel = np.ones((2,2), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        self.image = image

    def thick_font(self):
        image = cv2.bitwise_not(self.image)
        kernel = np.ones((2,2), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        self.image = image
    
    def remove_borders(self):
        contours, hierarchy = cv2.findContours(self.image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_sorted = sorted(contours, key=lambda x:cv2.contourArea(x))
        largest_bounding_box = contours_sorted[-1]
        x,y,w,h = cv2.boundingRect(largest_bounding_box)
        crop = self.image[y:y+h, x:x+w]
        self.image = crop
    
    def add_borders(self):
        color = [255, 255, 255]
        top, bottom, left, right = [150]*4
        image_with_border = cv2.copyMakeBorder(self.image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        self.image =  image_with_border
    
    
        # Rotation and deskewing
    # remove border before using this
    #https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df

    def getSkewAngle(cvImage) -> float:
        # Prep image, copy, convert to gray scale, blur, and threshold
        newImage = cvImage.copy()
        if len(newImage.shape) == 3 and newImage.shape[2] == 3: # Check if image is color, i might remove this later
            gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
        else:
            gray = newImage.copy()
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
        #print (len(contours))
        minAreaRect = cv2.minAreaRect(largestContour)
        cv2.imwrite("temp/boxes.jpg", newImage)
        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[-1]
        #print(angle)
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


    def deskew(self):
        angle = self.getSkewAngle(self.image)
        if abs(angle) == 90:                    # må være litt obs på dette med 90%
            pass
        else:
            self.image =  self.rotateImage(self.image, -1.0 * angle)
    
    



