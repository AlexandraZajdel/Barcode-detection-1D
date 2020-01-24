import cv2

def image_preprocessing(image):
    # convert to grayscale
    image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

    # apply gradient filter - Scharr filter; ddepth: 4-byte floating point
    gradient_x = cv2.Sobel(src=image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradient_y = cv2.Sobel(src=image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract gradients
    image = cv2.subtract(gradient_x, gradient_y)
    image = cv2.convertScaleAbs(image)

    # denoising
    image = cv2.GaussianBlur(image, (9, 9), 2)

    # thresholding
    _, image = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)

    # find rectangle
    # construct a closing kernel and apply it to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # perform series of erosions and dilations
    image = cv2.erode(image, None, iterations=4)
    image = cv2.dilate(image, None, iterations=4)

    return image