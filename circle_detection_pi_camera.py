# import Piccamera2 class frompiccamera module
from picamera2 import Picamera2
# import opencCV library
import cv2
# import numpy 
import numpy as np
# create piccam2 object from Piccamera2 class
picam2 = Picamera2()
# pass the precongigured settings for camera 
picam2.configure(picam2.create_preview_configuration())
# start the camera 
picam2.start()

# keep running the camera until user presses the key 
while True:
     # start capturing the images from live stream of camera
    frame = picam2.capture_array()
    # convert each frame from RGB to BGR color doamin to match with opnecv environment
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #convert image to GRAY format 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Apply the median blur
    gray = cv2.medianBlur(gray, 5)
    # detect the circles in each frame usinfg HOUGH GRADIENT
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=100,
        param1=100,
        param2=30,
        minRadius=20,
        maxRadius=100
    )
 # if circles are found 
    if circles is not None:
        circles = np.uint16(np.around(circles))
      # detect all the circles in frame
        for c in circles[0, :]:
            x, y, r = c
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)
  # display the image
    cv2.imshow("Circle Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
picam2.stop()
