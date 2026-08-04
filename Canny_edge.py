# import opnecv library
import cv2
# read the image 
image=cv2.imread("images.jpg")

# convert the image into gray scale 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#Applied Gaussian blur to gray scale and finding edges

Gauss_image=cv2.GaussianBlur(gray_image,(5,5),0)

# use gradient detection range in between 150 to 255
edge_image=cv2.Canny(gray_image,150,255)
# open the following windows to show different types of images
cv2.imshow("Original Image",image)
cv2.imshow("Gray Image",gray_image)
cv2.imshow("Edge Image",edge_image)
cv2.imshow("Gaussian Edge Image",edge_blur_image)

# wait until user presses the key 
cv2.waitKey(0)
cv2.destroyAllWindows()
