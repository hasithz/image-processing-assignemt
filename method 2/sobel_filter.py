import numpy as np
from sobelX import sobel_filterX
from sobelY import sobel_filterY


def sobel_filter(frame,image,val1=1,val2=9):

	image_row, image_col = frame.shape
	kernel_row, kernel_col = 3,3

	output = np.zeros(image.shape)
	pad_height = int((kernel_row - 1) / 2)
	pad_width = int((kernel_col - 1) / 2)

	padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)),np.ubyte)
	padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = frame

	Xcomp = sobel_filterX(frame.copy(),val1,val2)
	Ycomp = sobel_filterY(frame.copy(),val1,val2)

	# return Xcomp, Ycomp
	XS_frame = np.array(Xcomp,dtype=np.uint8)
	YS_frame = np.array(Ycomp,dtype=np.uint8)
	# return XS_frame

	gradient_magnitude = np.sqrt(np.square(YS_frame) + np.square(XS_frame))
	gradient_magnitude *= 255.0 / gradient_magnitude.max()

	gradient_direction = np.arctan2(YS_frame, XS_frame)

	gradient_direction = np.rad2deg(gradient_direction)
	gradient_direction += 180

	return gradient_magnitude, gradient_direction