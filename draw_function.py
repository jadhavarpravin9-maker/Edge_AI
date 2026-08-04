# import the opencv libraray
import cv2
# read the image into image object
image=cv2.imread("image1.jpg")
# creating the line between two points on images first point is located at (x1,y1) that is (293,283) and (x2,y2) that is (613,300) and (0,255,0) means green color 4 is thicknees of line
image=cv2.line(image,(293,283),(613,300),(0,255,0),4)

# two circles are drawn around the images one circle with centre around (613,300) and radius of 30 and another one with centre around (293,283) and radius of 30 with blue color
image=cv2.circle(image,center=(613,300),radius=30,color=(255,0,0),thickness=4)
image=cv2.circle(image,center=(293,283),radius=30,color=(255,0,0),thickness=4)

# reactangle  is drwan between (x1,y1) top left (495,140) and bottom right (580,190) bottom right
image=cv2.rectangle(image,(495,140),(580,190),(0,255,255),4)

# open the image and wait till user press key
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
