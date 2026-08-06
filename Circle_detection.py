# import opencv library
import cv2
# import numpy library
import numpy as np
# read the image and store information in img variable 
image=cv2.imread("image.jpg")
# convert the given image to gray 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Apply gaussian blurr to given image 
gray_image = cv2.GaussianBlur(gray_image, (9,9), 2)
# with below function it will caany edge detection is appied and voting mechnanism is used for determaing the circle centre 
circles=cv2.HoughCircles(gray_image,cv2.HOUGH_GRADIENT,dp=1,minDist=100,param1=100,param2=50,minRadius=10,maxRadius=60)
# if circle is found execute below part
if circles is not None:
    circles=np.uint16(np.around(circles))
    # x,y,z=circles[0][0]
    # cv2.circle(image,(x,y),z,(0,255,0),2)
    # cv2.circle(image,(x,y),2,(0,0,255),3)
# measure number of circles 
    for circle in circles[0, :]:
        x, y, r = circle
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)


    cv2.imshow("Detected Circle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles detected")
