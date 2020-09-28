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


webCam = "https://192.168.8.102:8080/video"

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	
	scale_percent = 100
	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dsize = (width, height)
	frame = cv2.resize(frame, dsize)

	H = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV_FULL)
	# H = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	
	frame2 = threshold(H[:,:,1].copy(),120,255)
	frame3 = threshold_inv(frame[:,:,1].copy(),70,255)
	frame4 = threshold(frame[:,:,0].copy(),0,100)
	frame2 = np.array(frame2,np.uint8)
	frame3 = np.array(frame3,np.uint8)
	frame4 = np.array(frame4,np.uint8)

	frame2 = median_filter(frame2,filter_size = 3,plot=False)
	frame3 = median_filter(frame3,filter_size = 3,plot=False)
	frame4 = median_filter(frame4,filter_size = 5,plot=False)
	
	frame3 = blacker(frame3,300)
	# frame3,a = sobel(frame3,True)
	frame3 = gaussian(frame3.copy(),9,plot=False)
	# frame4 = laplacian(frame2)

	a = pixel_count(frame3)
	b = pixel_count(frame4)
	# print('a',a,'\nb',b)
	
	ratio_full = (a/b)*100
	if ratio_full >= 80:
		print('ratio_full',ratio_full,'%')
		drawer(frame4)
		

	# frame3 = np.array(frame3,np.uint8)
	cv2.imshow('frame2',frame2)
	cv2.imshow('frame3',frame3)
	# cv2.imshow('HSV',H[:,:,0])
	cv2.imshow('original',frame4)
	# cv2. waitKey(0)
	if cv2.waitKey(1) & 0xff == ord("q"):
		break	