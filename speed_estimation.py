# import opencv module
import cv2
# import math module
import math
# import YOLO class from ultralytics
from ultralytics import YOLO
# video path for which speed detection is performed
VIDEO_PATH = "cars.mp4"
# YOLO model to be used
MODEL_PATH = "yolo26n.pt"   
# processed video path 
OUTPUT_PATH = "speed_estimation.mp4"

# confidance score greater than 0.35 will be accepted for any classification 
CONFIDENCE = 0.35
# a horizontal line is drwan at this particular location 
LINE_Y = 300
#per pixel distance covered in meter 
METER_PER_PIXEL = 0.032   
#  only detect car , motorcycle , bus , truck 
VEHICLE_CLASSES = {2, 3, 5, 7}   

# create object froM YOLO class
model = YOLO(MODEL_PATH)
#create a variable for image capturing 
cap = cv2.VideoCapture(VIDEO_PATH)
# check for error condintion while reading the cideo file 
assert cap.isOpened(), "Error reading video file"
# measure width and height from frame
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# calculate frame per second if value is zero then assign default fps 
fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25.0
# create output path for saving processed video 
video_writer = cv2.VideoWriter(
    OUTPUT_PATH,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

# create dictionary for storing values for last frame object details 
prev_centers = {}         
# create dictionary for storing speeds of object detected in previous frame
prev_speeds = {}  
# create dictionary for storing the vechicles which are crossed the line 
crossed_line = {}       
# display the speed of the tracked vechocles 
display_speed = {}       
# dictionary for storing s which side of the counting line the vehicle was on in the previous frame
prev_side = {}             

# start analysing the video 
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Video frame is empty or processing completed.")
        break
   # create a line in frame if valid frame is there 
    cv2.line(frame, (0, LINE_Y), (w, LINE_Y), (255, 0, 0), 3)
    cv2.putText(
        frame,
        "Detection Line",
        (10, LINE_Y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )
     # YOLO wil start its work by detecting objects , assigning IDs, Trackomng objects 
    results = model.track(frame, persist=True, conf=CONFIDENCE, verbose=False)
     # start processing bounding boxes for object detected
    if results and results[0].boxes is not None:
        boxes = results[0].boxes
      # extract bouding boxes 
        xyxy = boxes.xyxy.cpu().numpy() if boxes.xyxy is not None else []
        # extract class ids
        cls_ids = boxes.cls.cpu().numpy().astype(int) if boxes.cls is not None else []
        #  extract track ids
        track_ids = boxes.id.cpu().numpy().astype(int) if boxes.id is not None else None
        
         
        if track_ids is not None:
          # combine all the data 
            for box, cls_id, track_id in zip(xyxy, cls_ids, track_ids):
              # check if clss id is presnt in vechicle class which is already defined
                if cls_id not in VEHICLE_CLASSES:
                    continue
                # 
                x1, y1, x2, y2 = map(int, box)
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                  # extract box corner 
                class_name = model.names.get(cls_id, str(cls_id))
                 # check wether object has  crossed the line or not
                current_side = cy < LINE_Y  
                 # check is same vechicle was present in previoius frame 
                if track_id in prev_centers:
                  # extract the previous frame pixel co-ordinates
                    px, py = prev_centers[track_id]
                     # find the distance between pixel co-ordinates between current frame and previous frame 
                    pixel_distance = math.sqrt((cx - px) ** 2 + (cy - py) ** 2)
                   # calculate the actual distance 
                    distance_m = pixel_distance * METER_PER_PIXEL
                    speed_mps = distance_m * fps
                    speed_kmph = speed_mps * 3.6
                     # display the avg speed 
                    if track_id in prev_speeds:
                        speed_kmph = 0.7 * prev_speeds[track_id] + 0.3 * speed_kmph

                    prev_speeds[track_id] = speed_kmph
                 # check the vechicle position in previous frame 
                if track_id in prev_side:
                  # has vechicle crossed line , vehcile needs to be appread in prevoiuos to determine wether it has crossed the line or not 
                    if prev_side[track_id] != current_side and not crossed_line.get(track_id, False):
                        crossed_line[track_id] = True
                        display_speed[track_id] = prev_speeds.get(track_id, 0.0)
         
                prev_side[track_id] = current_side
                prev_centers[track_id] = (cx, cy)

                if crossed_line.get(track_id, False):
                    label = f"ID {track_id} {class_name} {display_speed[track_id]:.1f} km/h"
                else:
                    label = f"ID {track_id} {class_name}"
               
                cv2.putText(
                    frame,
                    label,
                    (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )

    video_writer.write(frame)
    cv2.imshow("Vehicle Speed Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
