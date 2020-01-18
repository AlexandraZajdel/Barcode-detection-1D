import cv2
import numpy as np

def find_bounding_box(image):
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if not contours: 
        # if there is no rectangles
        return None

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[0]

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(contours)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # return only one (the largest) bounding box
    return box