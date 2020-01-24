# 1D Barcode Detection
Detect barcode in the image or via web camera. Use image processing techniques. 

## Description
An input image is preprocessed according to the methodology listed below:
1) Grayscale image
2) Gradient calculation using Sobel filter
3) Gaussian blur (9x9 kernel)
4) Binary threshold at 220 intensity
5) Morphology using 21x7 kernel as structuring element
6) Series of erosion and dilation.

In the next step, the biggest rectangle countour is found using <b>findcontours()</b> from OpenCV library. 

Only one barcode in the image is recommended. 

## Sneak Peek
<p float="left">
<img src="results/example1.jpg" width=300> 
<img src="results/example2.jpg" width=300>
</p>
<p float="left">
<img src="results/example3.png" width=300> 
<img src="results/example4.jpg" width=300>
</p>

### Real-time results

## Project structure 
```bash
Barcode_detection/
├── README.md
├── requirements.txt
├── data
│   └── Barcode
│       └── passed          # a part of credited dataset
├── results                 # images with successfully detected barcodes
└── scripts
    ├── main.py             # the core of the project 
    ├── detection.py        # module with detection functions   
    └── preprocessing.py    # module with image preprocessing

```

## Setup 
To run this project on <b> Linux</b> type in your terminal:

```bash
$ git clone https://github.com/AleksandraPestka/Barcode-detection-1D.git
```
Use the package manager <b>pip</b> to install requirements (virtualenv recommended)
```bash
$ pip install -r requirements.txt
```
Move to script folder
```bash
$ cd scripts
```
Run project using your locally saved images: <br>

```bash
$ python main.py -m Locally -d DATA_DIRECTORY -s SAVE_DIRECTORY
```
DATA_DIRECTORY: path to folder which contains your images; one can use provided dataset in: <i>"../data/Barcode/passed/"</i> 
<br>SAVE_DIRECTORY (optionally): path to folder to save processed images; one can use: <i> "../results/" </i>


Or run project in real-time using web camera
```bash 
$ python main.py -m Real-time
```
## Difficulties
The algorithm is quite straightforward and based on image processing techniques, thus as a consequence it is not sufficiently robust to:
- blurry images<br>
<img src="results/failed3.jpg" width=200>
- images with many barcodes<br>
<img src="results/failed1.jpg" width=200>
- images with granulated structure<br>
<img src="results/failed2.jpg" width=200>
- images with a lot of text (no zoom in on barcode) <br>
<img src="results/failed4.jpg" width=200>

One of the ideas of improving algorithm's performance is to combine it with machine learning techniques such as Convolutional Neural Network.
Thanks to that, it would be general-purpose and robust to constraints described above. Moreover, the most desired feature would be also decoding the barcode. One of the libraries which provide such function is for example <i>pyzbar.</i> 

## Author
Created by Aleksandra Pestka

## Sources
This project is inspired by the blog post: <br>
- https://www.pyimagesearch.com/2014/11/24/detecting-barcodes-images-python-opencv/

<br> The source of the dataset is credited to: <br>
- Robust Angle Invariant 1D Barcode Detection
Alessandro Zamberletti, Ignazio Gallo and Simone Albertini
Proceedings of the 2nd Asian Conference on Pattern Recognition (ACPR), Okinawa, Japan, 2013

<br> Other publication: <br>
- Neural Image Restoration For Decoding 1-D Barcodes Using Common Camera Phones
Alessandro Zamberletti, Ignazio Gallo, Moreno Carullo and Elisabetta Binaghi
Computer Vision, Imaging and Computer Graphics. Theory and Applications, Springer Berlin Heidelberg, 2011

