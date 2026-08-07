# import opencv module
import cv2
# import time module
import time
# this parameters are used by resize function to rescale along x and y axis
WIDTH=620
HEIGHT=480
# store the image information
image=cv2.imread("image1.jpg")
# resize the image by scaing the WIDTH and HEIGHT by factor fx and fy
resize_img=cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# display the original image
cv2.imshow("Original Image",image)
# display resized umage
cv2.imshow("Resized Image",resize_img)
# wait for 3 seconds in beween two windows
time.sleep(3)
# wait for user key to press
cv2.waitKey(0)
cv2.destroyAllWindows()
