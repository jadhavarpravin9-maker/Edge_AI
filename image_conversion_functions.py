# import opencv libraray 
import cv2
# import time module 
import time
# read the image
image=cv2.imread("image1.jpg")
# convert the read image from B.G, R to R,G, B by deafault opencv reads image IN B,G,R format
rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# convert the image into GRAY color 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#gray_image=cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)
# convert the image into HSV format
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# convert the image into HLS format 
hsl_image=cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
# display the BGR converted image
cv2.imshow("BGR image",image)
# display the RGB converted image
cv2.imshow("RGB Image",rgb_image)
# wait for3 seconds until this window opens
time.sleep(3)
#open gray image window 
cv2.imshow("GRAY Image",gray_image)
# wait for 3 seonds to open this window 
time.sleep(3)
# open HSV image window 
cv2.imshow("HSV Image",hsv_image)
# wait for 3 seconds until this window opens
time.sleep(3)
# wait for user to press any key 
cv2.imshow("HSL Image",hsl_image)
time.sleep(3)
cv2.waitKey(0)
