#import opencv module 
import cv2
# import time module 
import time

# read image 
image=cv2.imread("image1.jpg")
# rotate the image by 90 degree to right 
rotate_image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
#rotate_image=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
#rotate_image=cv2.rotate(image,cv2.ROTATE_180)
# display the original image
cv2.imshow("Original Image",image)
#  display the rotated image
cv2.imshow("Rotated Image",rotate_image)
# hold the screen for 2 seconds
time.sleep(2)
# wait until user presses key
cv2.waitKey(0)
cv2.destroyAllWindows()
