# import Piccamera Class for raspberry pi camera detection
from picamera2 import Picamera2
# import opencv module
import cv2
# import numpy
import numpy as np
# create object picam2 using Picamera class
picam2=Picamera2()
# pass the configuration for camera such as resolution 
picam2.configure(picam2.create_preview_configuration())
# start the camera 
picam2.start()

# face cascade and eye cascade learns from xml files , xml file containts all the leaned data 
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

# below loop will keep running the camera and will keep detecting faces and eyes 
while True:

    frame=picam2.capture_array()

    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detecting Face
    faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5,minSize=(80,80))
    #it is going to return [x, y, w, h]

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

    #Detecting Eye

    eyes=eye_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=8,minSize=(20,20))
    #it is going to return [ex, ey, ew, eh]

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    cv2.imshow("Detected Face & eyes",frame)

    if cv2.waitKey(1) == 27:
        break
# wait until user presses any key
cv2.destroyAllWindows()
picam2.stop()
