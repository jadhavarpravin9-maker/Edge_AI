# import YOLO class  from ultralytics module
from ultralytics import YOLO
# import opencv module
import cv2

# crreate YOLO  object
model=YOLO("yolo26n.pt")
# create object for this function
cap=cv2.VideoCapture("cars.mp4")
# check for any error while opening the video
assert cap.isOpened(), "Error Reading the video"

# capture width , height , fps for video frames
w, h, fps=(int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# write this to oputput folder 
video_writer=cv2.VideoWriter("Tracked Vehicle.mp4",cv2.VideoWriter_fourcc(*'mp4v'),fps,(w,h))

# start processing on video 
while cap.isOpened():
 # check for success or failure for video opening 
	success, frame=cap.read()
  # check the condition for video opening 
	if not success:
		print("Video is not opened/done")
		break
   # start tracking the vechicle using the YOLO algorithm , where YOLO is applied to detect objects and track acrtoss the frames 
	tracking=model.track(frame,persist=True,tracker="bytetrack.yaml")	#ByteTrack(Fast & Accurate), Bot-SORT track(Default)
    # retun the processed frame information 
	annotate_frame=tracking[0].plot()
   # write it to processed output frame 
	video_writer.write(annotate_frame)

# wait until user presses any key 
cap.release()
video_writer.release()
cv2.destroyAllWindows()
