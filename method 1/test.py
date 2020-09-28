import cv2
import numpy as np
import matplotlib.pyplot as plt

from threshold import threshold as threshold
from threshold import threshold_inverse as threshold_inv
from filters import median_filter as median_filter
from filters import make_black_filter as blacker
from filters import sobel_filter as sobel
from filters import laplacian_filter as laplacian
from filters import gaussian_blur as gaussian
from pix_count import pixel_count
from draw_cont import drawer

path = 'PICS/26.JPG' # yellow background


cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    
    scale_percent = 20
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dsize = (width, height)
    frame = cv2.resize(frame, dsize)

    frame1 = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    frame4,aaaaa = sobel(frame1)
    print (frame4[0:10,0:10])
    cv2.imshow('frame2',frame1)
    cv2.imshow('original',frame4)
    cv2. waitKey(0)
    # if cv2.waitKey(1) & 0xff == ord("q"):
        # break 