# import opencv library
import cv2
# print the opencv version
print(cv2.__version__)
# load the image information 
image=cv2.imread("image.jpeg")
# print the image information
print(image)
# display the image
cv2.imshow("Aston martin",image)
# wait for key to press
cv2.waitKey(0)
