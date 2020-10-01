import cv2
import numpy as np

from gaussian import gaussian_blur
from threshold import threshold
from suppression import non_max_suppression
from pix_count import pixel_count
from sobel_filter import sobel_filter

# path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/5.JPG'
# path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/vid1.mp4'
# cap = cv2.VideoCapture(path)

def all_filter(frame,scale_percent = 20,frame_val=2,thresh1_val =170, gaussian1_val= 40, sobel_val1 = 13, sobel_val2 = 30, thresh_val =70):

	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dsize = (width, height)
	frame = cv2.resize(frame, dsize)
	# frame = frame[:,:,2]
	frame1 = frame.copy()
	
	thresh1 = threshold(frame1[:,:,frame_val].copy(),thresh1_val)
	thresh1 = np.array(thresh1,np.uint8)

	frame1 = cv2.cvtColor(frame1,cv2.COLOR_RGB2GRAY)

	gaussian1 = gaussian_blur(frame1.copy(),gaussian1_val)
	gaussian1 = np.array(gaussian1,np.uint8)

	iamge1 = np.zeros((gaussian1.shape[0],gaussian1.shape[1]),np.uint8)

	frame2,direction = sobel_filter(gaussian1.copy(),iamge1,sobel_val1,sobel_val2)
	frame2 = np.array(frame2,dtype=np.ubyte)
	direction = np.array(direction,dtype=np.ubyte)

	thresh = threshold(frame2,thresh_val)
	thresh = np.array(thresh,np.uint8)

	frame3 = non_max_suppression(thresh,direction)
	frame3 = np.array(frame3,dtype=np.uint8)

	a = pixel_count(thresh1)
	b = pixel_count(frame3)

	c = (b-a)/b*100


	return frame1, thresh1, frame3, a, b, c
