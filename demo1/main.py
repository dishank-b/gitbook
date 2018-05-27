import numpy as np
import cv2
import operations as op
from scipy import misc
import matplotlib.pyplot as plt

#--------Load Image------------#
org_img = misc.imread("Plaque.jpg")

print "Displaying Original Image......."
plt.figure(1)
plt.title("Original Image")
plt.imshow(org_img)


#------- GrayScale Image-------#
print "Converting to GrayScale and Displaying...."

gray_img = op.bgr_to_gray(org_img)

plt.figure(2)
plt.title("GrayScale Image")
plt.imshow(gray_img, cmap='gray')

print "Done"
#------------------------------#


#-------- Adding Gaussian Noise-------#

print "Image Denoising......."
noise_img = op.gaussNoise(gray_img, 5)

# Denoising Image
gauss_filter_img = op.gaussianBlur(noise_img, stddev=4, kern=3)  # only use square kernel, of odd size
median_filter_img = op.medianBlur(noise_img, kern=5)

plt.figure(3)
plt.subplot(2,2,1)
plt.title("Noise Image")
plt.imshow(noise_img, cmap='gray')

plt.subplot(2,2,2)
plt.title("Median Filter Image")
plt.imshow(median_filter_img, cmap='gray')

plt.subplot(2,2,3)
plt.title("Gaussian Filter Image")
plt.imshow(gauss_filter_img, cmap='gray')

#------------------------------#


#------- Edge Detection using Filters----------#
print "Edge Detection using Sobel and Prewitt Detectors......"
x_grad, y_grad, mag_img = op.edge(gray_img, operator="prewitt")  # get operator="sobel" for testing sobel

plt.figure(4)
plt.subplot(2,2,1)
plt.title("X gradient Image")
plt.imshow(x_grad, cmap='gray')

plt.subplot(2,2,2)
plt.title("y gradient Image")
plt.imshow(y_grad, cmap='gray')

plt.subplot(2,2,3)
plt.title("Edge Image")
plt.imshow(mag_img, cmap='gray')

print "Done"
#------------------------------#

#-----------Edge Detection using LoG------------#
print "Edge Detection using laplacian of gaussian......."
log_img, edgy = op.LoG(gray_img, 5,11)

plt.figure(7)
plt.subplot(2,1,1)
plt.title("LoG Image")
plt.imshow(log_img, cmap='gray')

plt.subplot(2,1,2)
plt.title("Edge Image")
plt.imshow(edgy, cmap='gray')

print "Done"
#-----------Corner Detection----------#
print "Finding Corners..........."
corner_img = op.findCorners(gray_img, thresh=10000000)

plt.figure(5)
plt.title("Corner Image")
plt.imshow(corner_img, cmap='gray')


print "Done"
#----------------------------------------#


#-----------Image Enhancement------------#
print "Performing Image Enhancement........." 
enh_img = op.enhance(gray_img, method="histogram_equal")

plt.figure(6)
plt.title("Enhance Image")
plt.imshow(enh_img, cmap='gray')

plt.show()

#----------------------------------#





