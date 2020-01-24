import os
import glob
import argparse
import logging

import cv2
import numpy as np

from preprocessing import image_preprocessing
from detection import find_bounding_box

def command_line_args():
    parser = argparse.ArgumentParser(prog='Barcode 1D detection',
                                     description='Detect the barcode in the image \
                                        using image processing techniques')
    parser.add_argument("-m", "--mode",
                        required=True,
                        choices=['Locally', 'Real-time'],
                        help='Choose a mode for program - load local images or \
                            run real-time detection using web camera')
    parser.add_argument("-d", "--data_directory",
                        required=('--mode' == 'Locally'),
                        type=str,
                        help='Provide images directory; required if mode == Locally')
    parser.add_argument("-s", "--save_directory",
                        required=False,
                        type=str,
                        help="Provide directory to save barcodes with bounding boxes")
    args = vars(parser.parse_args())
    return args

def save_image(image, directory, filename):
    cv2.imwrite(os.path.join(directory, filename), image)
    logging.info(f'\tProcessed image saved in: {directory}')

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    args = command_line_args()

    if args['mode'] == 'Locally':
        logging.info(f'\nLocal images detection mode.\
                    \nPress Q to move on to the next image.\
                    \nPress E to exit.')

        extensions = ['png', 'jpg', 'gif', 'jpeg']
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(
                args['data_directory'], '*.' + ext)))

        for filepath in files:
            img_orig = cv2.imread(filepath)
            img_processed = image_preprocessing(img_orig)
            box = find_bounding_box(img_processed)

            if box is not None:
                img_box = cv2.drawContours(img_orig, [box], -1, (0, 255, 0), 3)
                
                if args['save_directory'] != None:
                    save_image(img_box, args['save_directory'], 
                               os.path.basename(filepath))

                cv2.imshow("Barcode detection", img_box)
                key = cv2.waitKey(0)
                if key == ord('q'):
                    continue
                elif key == ord('e'):
                    break

            else: logging.info(f'\tNo barcode detected for: {os.path.basename(filepath)}')

    elif args['mode'] == 'Real-time':
        logging.info(f'\tReal-time detection mode. \nPress Q to interrupt.')

        stream = cv2.VideoCapture(0)
        while True:
            (grabbed, frame) = stream.read()
            img_processed = image_preprocessing(frame)
            box = find_bounding_box(img_processed)

            if box is not None:
                cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)

            cv2.imshow("Barcode detection", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        stream.release()

    cv2.destroyAllWindows()