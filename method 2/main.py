import cv2
import numpy as np
# import gau
# import convolution
from gaussian import gaussian_blur

from threshold import threshold
from suppression import non_max_suppression
from pix_count import pixel_count
from sobel_filter import sobel_filter

path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/25.JPG'
# path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/vid1.mp4'
cap = cv2.VideoCapture(path)

while True:
	ret, frame = cap.read()
	
	scale_percent = 20

	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dsize = (width, height)
	frame = cv2.resize(frame, dsize)
	# frame = frame[:,:,2]
	frame1 = frame.copy()
	
	thresh1 = threshold(frame1[:,:,2].copy(),170)
	thresh1 = np.array(thresh1,np.uint8)

	frame1 = cv2.cvtColor(frame1,cv2.COLOR_RGB2GRAY)
	# convolution1 = convolution.convolution(frame1.copy(),kernel,0)
	# convolution1 = np.array(convolution1,np.uint8)
	# padded_image = np.zeros((width + (2 * 9), height + (2 * 9)),np.ubyte)
	# padded_image[9:padded_image.shape[0] - 9, 9:padded_image.shape[1] - 9] = frame1

	#gaussian blur works don't dlt
	gaussian1 = gaussian_blur(frame1.copy(),40)
	gaussian1 = np.array(gaussian1,np.uint8)

	iamge1 = np.zeros((gaussian1.shape[0],gaussian1.shape[1]),np.uint8)

	frame2,direction = sobel_filter(gaussian1.copy(),iamge1,13,30)
	frame2 = np.array(frame2,dtype=np.ubyte)
	direction = np.array(direction,dtype=np.ubyte)
	# print (direction)
	# break
	thresh = threshold(frame2,70)
	thresh = np.array(thresh,np.uint8)

	frame3 = non_max_suppression(thresh,direction)
	frame3 = np.array(frame3,dtype=np.uint8)
	

	# frame3 = threshold2(frame3,5, 20,50)
	# print(frame3)
	# break
	# thresh = threshold.threshold(frame2,25)
	# thresh = np.array(thresh,np.uint8)
	cv2.imshow('output',frame1)
	cv2.imshow('output1',thresh1)
	cv2.imshow('image',frame3)

	a = pixel_count(thresh1)
	b = pixel_count(frame3)

	# print ('a',a)
	# print ('b',b)
	c = (b-a)/b*100
	if c >=80:
		print ('precentage of filled bottle ',c)

	cv2. waitKey(0)
	# if cv2.waitKey(1) & 0xff == ord("q"):
		# break


