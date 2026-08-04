# import camera module for using raspberry pi module 
from picamera2 import Picamera2
# import opencv module
import cv2

# create object from Piccamera2() module
picam2 = Picamera2()
# by this decide resolution , frame rate , pixel format , display mode
picam2.configure(picam2.create_preview_configuration())
# start the camera module 
picam2.start()
# After starting ths camera module be in below loop until user presses some key for breaking the while loop 
while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
picam2.stop()
