import cv2
import numpy as np
import glob
import argparse

def command_line_args():
    parser = argparse.ArgumentParser(prog='Barcode 1D detection',
                                     description='Detect the barcode in the image using image processing techniques')
    parser.add_argument("-m", "--mode", 
                        required=True, 
                        choices=['Locally', 'Real-time'],
                        help='Choose a mode for program - load local images or run real-time detection using web camera')
    parser.add_argument("-d", "--directory",
                        required=('--mode'=='Locally'),
                        type=str,
                        help='Provide images directory; required if mode == Locally')
    args = vars(parser.parse_args())
    return args

def load_image(path):
    return cv2.imread(path)













if __name__ == "__main__":
    args = command_line_args()

    if args['mode']=='Locally':
        files = glob.glob(args['directory']+'*.jpg')
        print(files)