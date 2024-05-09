from abc import ABC
from PIL import Image
import cv2
from matplotlib import pyplot as plt
import numpy as np


class Filter(ABC):
    """Filter is an abstract class that defines the interface for all filters

    Args:
        ABC (_type_): _description_
    """

    def __call__(self, image):
        pass


class Invert_image(Filter):
    """Invert the image, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        return cv2.bitwise_not(image)


class grayscale(Filter):
    """Grayscale the image, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


class binarize(Filter):
    """Binarize the image, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        try:  # if the image is already grayscale, this will throw an error
            filter: Filter = grayscale()
            image = filter(image)
        except:
            pass

        thresh, im_bw = cv2.threshold(
            image, 200, 230, cv2.THRESH_BINARY
        )  # must calibrate these values
        return im_bw


class remove_noise(Filter):
    """Remove noice from the image, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)  # must calibrate these values
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 3)
        return image


class Thin_font(Filter):
    """Make text thinner, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        image = cv2.bitwise_not(image)
        kernel = np.ones((2, 2), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return image


class Thick_font(Filter):
    """makes text bold, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        image = cv2.bitwise_not(image)
        kernel = np.ones((2, 2), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return image


class remove_borders(Filter):
    """Remove borders, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        contours, hierarchy = cv2.findContours(
            image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x))
        largest_bounding_box = contours_sorted[-1]
        x, y, w, h = cv2.boundingRect(largest_bounding_box)
        crop = image[y : y + h, x : x + w]
        return crop


class add_borders(Filter):
    """add boarders, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        color = [255, 255, 255]
        top, bottom, left, right = [150] * 4
        image_with_border = cv2.copyMakeBorder(
            image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color
        )
        return image_with_border


class deskew(Filter):
    """rotates the image in necessary, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, image):
        angle = self.getSkewAngle(image)
        image = self.rotateImage(image, -1.0 * angle)
        return image

        # Rotation and deskewing
        # remove border before using this
        # https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df

    def getSkewAngle(self, cvImage) -> float:
        # Prep image, copy, convert to gray scale, blur, and threshold
        newImage = cvImage.copy()
        if (
            len(newImage.shape) == 3 and newImage.shape[2] == 3
        ):  # Check if image is color, i might remove this later
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
        contours, hierarchy = cv2.findContours(
            dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        for c in contours:
            rect = cv2.boundingRect(c)
            x, y, w, h = rect
            cv2.rectangle(newImage, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Find largest contour and surround in min area box
        largestContour = contours[0]
        # print (len(contours))
        minAreaRect = cv2.minAreaRect(largestContour)
        cv2.imwrite("temp/boxes.jpg", newImage)
        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[-1]
        # print(angle)
        if angle < -45:
            angle = 90 + angle
        return -1.0 * angle

    # Rotate the image around its center
    def rotateImage(self, cvImage, angle: float):
        newImage = cvImage.copy()
        (h, w) = newImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        newImage = cv2.warpAffine(
            newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
        )
        return newImage


# https://stackoverflow.com/questions/28816046/
# displaying-different-images-with-actual-size-in-matplotlib-subplot


class Display(Filter):
    """Displays the image, callable

    Args:
         image
    Returns:
        image
    """

    def __call__(self, im_data):

        dpi = 80

        height, width = im_data.shape[:2]

        # What size does the figure need to be in inches to fit the image?
        figsize = width / float(dpi), height / float(dpi)

        # Create a figure of the right size with one axes that takes up the full figure
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])

        # Hide spines, ticks, etc.
        ax.axis("off")

        # Display the image.
        ax.imshow(im_data, cmap="gray")

        plt.show()
