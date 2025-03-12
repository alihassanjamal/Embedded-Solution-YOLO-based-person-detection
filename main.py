import cv2
import numpy as np
import torch
import serial
from blynklib import Blynk
import pandas
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("E:\FreeLance Projects\PeopleCounting\peoplecounter-12351-firebase-adminsdk-1ahwx-e7b219c973.json")  # Replace with your service account JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://peoplecounter-12351-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

# YOLOv5 model configuration
yaml = 'E:\FreeLance Projects\PeopleCounting\yolov5s.yaml'
weights = 'E:\FreeLance Projects\PeopleCounting\yolov5s.pt'
conf_threshold = 0.5
device = 'cuda' if torch.cuda.is_available() else 'cpu'
box_index = torch.tensor([1, 2, 3, 4])
NoofPeople = 0;
# Replace 'YOUR_ESP32_CAM_IP' with the actual IP address of your ESP32-CAM
esp32_cam_url = 'http://YOUR_ESP32_CAM_IP/capture'

# Serial communication settings
arduino_port = 'COM5'  # Replace with the correct port for your Arduino
baud_rate = 230400;
ser = serial.Serial(arduino_port, baud_rate)
#load yolo5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.to(device).eval();

# Define a function to write data to Firebase
def write_to_firebase(data):
    ref = db.reference('/Number of People')  # Replace 'your-node' with the node in your database
    ref.set(data)

def detect_people(frame):
    results = model(frame)
    people_counter = 0;
    data_frame = results.pandas().xyxy[0];
    indexes = data_frame.index
    for index in indexes:
        # Find the coordinate of top left corner of bounding box
        x1 = int(data_frame['xmin'][index])
        y1 = int(data_frame['ymin'][index])
        # Find the coordinate of right bottom corner of bounding box
        x2 = int(data_frame['xmax'][index])
        y2 = int(data_frame['ymax'][index])

        # Find label name
        label = data_frame['name'][index]
        # Find confidance score of the model
        conf = data_frame['confidence'][index]
        text = label + ' ' + str(conf.round(decimals=2))

        if label == 'person':
            people_counter = people_counter + 1;
            if people_counter < 10:
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2);
                cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2,
                            (0, 255, 0), 2)
            if people_counter >= 10 and people_counter < 20:
                cv2.rectangle(frame, (x1,y1), (x2,y2), (255,255,0), 2);
                cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2,
                            (255, 255, 0), 2)
            if people_counter >= 20 and people_counter < 30:
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 2);
                cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2,
                            (0, 0, 255), 2)
    return people_counter  # Return bounding box coordinates
# Capture video from the default camera (index 0)
cap = cv2.VideoCapture(esp32_cam_url)


while True:
    # Capture frame-by-frame
     ret, frame = cap.read()

    # Detect people
     NoofPeople = detect_people(frame)

    #Send the number of people detected to Arduino serially
     ser.write(str(NoofPeople).encode())

    # Display the captured frame
     cv2.imshow('Frame', frame)

     write_to_firebase(NoofPeople)

    # Break the loop if 'q' is pressed
     if cv2.waitKey(1) & 0xFF == ord('q'):
       break