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

def all_filters(frame,scale_percent = 20, threshVal1 = 120, threshVal2 = 255,thresholdVal1_inv = 70,thresholdVal2_inv = 255,
				thresholdVal3 = 0, thresholdVal4 = 100,median_filter_size = 5,blackign =3):
	# ret, frame = cap.read()
	
	# print (frame.shape)
	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dsize = (width, height)
	frame = cv2.resize(frame, dsize)

	H = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV_FULL)
	# H = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	# print (frame.shape)
	frame2 = threshold(H[:,:,1].copy(),threshVal1,threshVal2)
	frame3 = threshold_inv(frame[:,:,1].copy(),thresholdVal1_inv,thresholdVal2_inv)
	frame4 = threshold(frame[:,:,0].copy(),thresholdVal3,thresholdVal4)
	frame2 = np.array(frame2,np.uint8)
	frame3 = np.array(frame3,np.uint8)
	frame4 = np.array(frame4,np.uint8)
	# print (frame4.shape)
	frame2 = median_filter(frame2,filter_size = median_filter_size,plot=False)
	frame3 = median_filter(frame3,filter_size = median_filter_size,plot=False)
	frame4 = median_filter(frame4,filter_size = median_filter_size,plot=False)
	# print (frame4.shape)
	frame3 = blacker(frame3,blackign)
	# frame3,a = sobel(frame3,True)
	frame3 = gaussian(frame3.copy(),9,plot=False)
	# frame4 = laplacian(frame2)

	a = pixel_count(frame3)
	b = pixel_count(frame4)
	
	if b !=0:
		ratio_full = (a/b+1)*100
	# print ('ammatasiri methnata wenakan enawa')
	return frame2, frame3, frame4, a,b, ratio_full
	