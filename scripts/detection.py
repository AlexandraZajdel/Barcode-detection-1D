import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def find_bounding_box(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours: 
        # if there is no rectangles
        return None

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(contours[0])
    box = np.int0(cv2.boxPoints(rect))

    # return only one (the largest) bounding box
    return box
