# import the opencv 
import cv2
# import the time module
import time
# read the original image
image=cv2.imread("images.jpg")
# kernel or matrix of 5 by 5 is created this kernel is used for averaging each pixel with nearby(5x5= 25 pixels) 
blur_image=cv2.blur(image,(5,5))
# this is same as that of blur only differance is for smoothening it stresses nearby pixels as compared to normal blur
Gauss_image=cv2.GaussianBlur(image,(5,5),0)
# thus blur uses middle value for smoothening the image
median_blur=cv2.medianBlur(image,5)
#this blur is used for most appropriate smmthning of image
bilateral_blur=cv2.bilateralFilter(image,7,100,100)

# display all the images
cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blur_image)
cv2.imshow("Gaussian Blur Image",Gauss_image)
cv2.imshow("Median Blur Image",median_blur)
cv2.imshow("Bilateral Blur Image",bilateral_blur)
# wait for user to press the key
cv2.waitKey(0)
cv2.destroyAllWindows()
