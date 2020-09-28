from convolusion import convolve as convolusion
from make_black import make_black
import numpy as np
import math
import matplotlib.pyplot as plt
from threshold import threshold as threshold

def median_filter(image,filter_size, plot=False):
	kernel1 = np.ones((filter_size,filter_size),dtype=np.int)
	image = np.array(image,dtype=np.int)
	output =  np.array(convolusion(image,kernel1),dtype=np.uint8)

	if plot:
		plt.imshow(output, interpolation='none', cmap='gray')
		plt.title("output ( {}X{} )".format(size, size))
		plt.show()

	return output

def make_black_filter(image,value):
	output = make_black(image,value)
	output = np.array(output, dtype=np.uint8)
	return output

def sobel_filter(image, convert_to_degree=False, plot=False):
	
	image = np.array(image,dtype=np.int)
	filter = np.array(([-1, 0, 1],
					   [-2, 0, 2],
					   [-1, 0, 1]),dtype=np.int)
	image_x = convolusion(image, filter)

	if plot:
		plt.imshow(image_x, interpolation='none', cmap='gray')
		plt.title("image_x ( {}X{} )".format(size, size))
		plt.show()

	image_y = convolusion(image, np.flip(filter.T, axis=0))

	if plot:
		plt.imshow(image_y, interpolation='none', cmap='gray')
		plt.title("image_y ( {}X{} )".format(size, size))
		plt.show()

	gradient_magnitude = np.sqrt(np.square(image_x) + np.square(image_y))
	gradient_magnitude *= 255.0 / gradient_magnitude.max()
	gradient_direction = np.arctan2(image_y, image_x)

	if convert_to_degree:
		gradient_direction = np.rad2deg(gradient_direction)
		gradient_direction += 180

	if plot:
		plt.imshow(gradient_magnitude, interpolation='none', cmap='gray')
		plt.title("gradient_magnitude ( {}X{} )".format(size, size))
		plt.show()

	return np.array(gradient_magnitude,dtype=np.uint8), gradient_direction

def laplacian_filter(image, plot=False):
	image = np.array(image,dtype=np.int)
	filter = np.array(([-1,-1,-1],
					   [-1, 8,-1],
					   [-1,-1,-1]),dtype=np.int)

	output = convolusion(image, filter)

	if plot:
		plt.imshow(output, interpolation='none', cmap='gray')
		plt.title("output ")
		plt.show()

	output = output - output.min()
	print (output.max())
	output = output/output.max()*255
	print (output.min())
	return np.array(output,dtype=np.uint8)

def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)


def gaussian_kernel(size, sigma=1, plot=False):

	kernel_1D = np.linspace(-(size // 2), size // 2, size)
	for i in range(size):
		kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
	kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

	kernel_2D *= 3.0 / kernel_2D.max()

	if plot:
		plt.imshow(kernel_2D, interpolation='none', cmap='gray')
		plt.title("Kernel ( {}X{} )".format(size, size))
		plt.show()

	return np.array(kernel_2D,dtype=np.int)


def gaussian_blur(image, kernel_size, plot=False):
	image  = np.array(image,dtype=np.int)
	kernel = gaussian_kernel(kernel_size, sigma=math.sqrt(kernel_size), plot=plot)
	blur   = np.array(convolusion(image, kernel),dtype=np.uint8)

	return np.array(threshold(blur,1,255),dtype=np.uint8)

