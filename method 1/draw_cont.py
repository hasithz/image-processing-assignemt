import numpy as np
import cv2 
from filters import laplacian_filter as laplacian
from filters import median_filter as median_filter

def drawer(image):

	image = np.array(image,np.int)
	new_image = laplacian(image)

	rows = new_image.shape[0]
	cols = new_image.shape[1]

	out = np.zeros((rows,cols,3),np.uint8)
	out[:,:,1] = new_image
	cv2.imshow('max',new_image)
	cv2.waitKey(0)
