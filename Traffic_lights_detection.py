
# mount the google drive 
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/MyDrive/Traffic_Light"
# install ultralytics module
!pip install ultralytics
# import YOLO class from ultralytics module 
from ultralytics import YOLO
# command for classifying the traffic light data using YOLOnano model and classification model pyotch library , this is training phase 
!yolo task=classify mode=train data="/content/drive/MyDrive/Traffic_Light" model="yolo11n-cls.pt" epochs=100 imgsz=224
# this is detection phase best.pt file utilised for predicting the data
!yolo task=detect mode=predict data="/content/drive/MyDrive/Traffic_Light/runs/classify/train/weights/best.pt" source = "/content/drive/MyDrive/Traffic_Light/test/red" save = True
# create model using best.pt
model = YOLO("/content/drive/MyDrive/Traffic_Light/runs/classify/train/weights/best.pt")
# predict the testing data using test.pt
results = model.predict(
    source="/content/drive/MyDrive/Traffic_Light/test/green/",
    imgsz=224
)
# iterate over the results 
for r in results:
    probs = r.probs
    print("Predicted:", r.names[probs.top1])
    print("Confidence:", float(probs.top1conf))
