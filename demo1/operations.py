import numpy as np
import cv2
from scipy import misc
import matplotlib.pyplot as plt

def bgr_to_gray(img):
	out = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
	# out[:,:] = 0.299*img[:,:,2] + 0.587*img[:,:,1] + 0.114*img[:,:,0] # using intensity = R*0.299 + G*0.587 + B*0.114
	out[:,:] = 0.2126*img[:,:,2] + 0.7152*img[:,:,1] + 0.0722*img[:,:,0] # using intensity = R*0.2126 + G*0.7152 + B*0.0722
	return out

def gaussNoise(img, stddev):
	gauss = np.random.normal(0,stddev,img.shape)
	out1 = img + gauss
	return out1


def medianBlur(img, kern):
	width, height = img.shape[1], img.shape[0]
	copy= np.array(img)
	out= np.array(img)
	arr = np.zeros((kern/2,copy.shape[1]))
	copy = np.concatenate((arr, copy, arr),axis=0)
 	arr = np.zeros((copy.shape[0],kern/2))
 	copy = np.concatenate((arr, copy, arr),axis=1)
 	for i in range(height):
 		for j in range(width):
 			out[i,j] = np.median(copy[i:i+kern/2+kern/2+1,j:j+kern/2+kern/2+1])
	return out

def gaussianVal(x,y,stddev):
	return np.exp(-(x**2+y**2)/(2*stddev**2))/(2*np.pi*stddev**2)

def gaussianBlur(img, stddev, kern):
	kernel  = [[gaussianVal(i-kern/2,j-kern/2,stddev) for i in range(kern)] for j in range(kern)]
	kernel = kernel/np.sum(kernel)
	width, height = img.shape[1], img.shape[0]
	copy= np.array(img)
	out= np.array(img)
	arr = np.zeros((kern/2,copy.shape[1]))
	copy = np.concatenate((arr, copy, arr),axis=0)
 	arr = np.zeros((copy.shape[0],kern/2))
 	copy = np.concatenate((arr, copy, arr),axis=1)
 	for i in range(height):
 		for j in range(width):
 			out[i,j] = np.sum(np.multiply(copy[i:i+kern/2+kern/2+1,j:j+kern/2+kern/2+1],kernel))
	return out

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def PSNR(Original,noisy):
	r_mse = RMSE(x,y)
	max_org = x.max()
	return 20*np.log10(max_org/r_mse)

def edge(img, operator="sobel"):
	grad_x = np.array(img)             # We could have done only like grad_x = img, but in that case, when later grad_x is changed 'for' loop then
	grad_y = np.array(img)			   # img is also changed, hence as grad_x and img refer to same object in that case. Hence in the main file
	mag = np.array(img)				   # gray_img is also chaged because again gray_img and img refer to same object when passed in function as argument.
	if operator=="prewitt":
		kernel_x= np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
		kernel_y= np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) # experiment with [[-1,-1,-1],[0,0,0],[1,1,1]]
	if operator=="sobel":
		kernel_x= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
		kernel_y= np.array([[1,2,1],[0,0,0],[-1,-2,-1]]) # experiment with [[-1,-1,-1],[0,0,0],[1,1,1]]
	for i in range(1,img.shape[0]-1):
		for j in range(1,img.shape[1]-1):
			grad_x[i,j] = np.sum(np.multiply(img[i-1:i+2,j-1:j+2],kernel_x)) 
			grad_y[i,j] = np.sum(np.multiply(img[i-1:i+2,j-1:j+2],kernel_y))
			mag[i,j] = np.sqrt(grad_x[i,j]**2+grad_y[i,j]**2)

	return grad_x, grad_y, mag

def log_val(x, y, stddev):
	# print x,y, -(1.0-float(x**2+y**2)/float(2*stddev**2))*np.exp(-(x**2+y**2)/(2*stddev**2))
	return -(1.0-float(x**2+y**2)/float(2*stddev**2))*np.exp(-(x**2+y**2)/(2*stddev**2))

def LoG(img, stddev, kern=5):
	kernel  = [[log_val(i-kern/2,j-kern/2,stddev) for i in range(kern)] for j in range(kern)]
	kernel = kernel/np.sum(kernel)
	log_img = np.array(img)
	edges = np.full(img.shape, 255)
	for i in range(kern/2,img.shape[0]-kern/2):
		for j in range(kern/2,img.shape[1]-kern/2):
			log_img[i,j] = np.sum(np.multiply(img[i-kern/2:i+kern/2+1,j-kern/2:j+kern/2+1],kernel))
			if log_img[i,j]==0:
				edges[i,j]=0

	return log_img, edges

def findCorners(img, thresh,kern=3, k=0.05):

	dy, dx = np.gradient(img)
	Ixx = dx**2
	Ixy = dy*dx
	Iyy = dy**2
	height = img.shape[0]
	width = img.shape[1]

	newImg = img.copy()

	#Loop through image and find our corners
	for y in range(kern/2, height-kern/2):
		for x in range(kern/2, width-kern/2):
			#Calculate sum of squares
			windowIxx = Ixx[y-kern/2:y+kern/2+1, x-kern/2:x+kern/2+1]
			windowIxy = Ixy[y-kern/2:y+kern/2+1, x-kern/2:x+kern/2+1]
			windowIyy = Iyy[y-kern/2:y+kern/2+1, x-kern/2:x+kern/2+1]
			Sxx = windowIxx.sum()
			Sxy = windowIxy.sum()
			Syy = windowIyy.sum()

			#Find determinant and trace, use to get corner response
			det = (Sxx * Syy) - (Sxy**2)
			trace = Sxx + Syy
			r = det - k*(trace**2)

			#If corner response is over threshold, color the point and add to corner list
			if r > thresh:
			    newImg[y-2:y+3,x-2:x+3]=0
	return newImg



def enhance(img, method="histogram_equal"):
	height, width = img.shape
	out = np.array(img)
	h = [0.0] * 256
	for i in range(height):
		for j in range(width):
			h[img[i, j]]+=1
	norm_hist = np.array(h)/(height*width)
	cumm_hist = np.array([sum(norm_hist[:i+1]) for i in range(len(norm_hist))])
	tf = np.uint8(255 * cumm_hist)
	for i in range(0, height):
		for j in range(0, width):
			out[i, j] = tf[img[i, j]]

	return out