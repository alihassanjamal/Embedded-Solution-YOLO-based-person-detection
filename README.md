# Embedded-Solution-YOLO-based-person-detection
 Person Detection System using YOLOv5 and Arduino to Trigger an Alarm
💡 Overview

This project is an AI-powered Person Detection System that leverages YOLOv5 for real-time object detection and integrates with Arduino to trigger an alarm when a certain number of people are detected. The system utilizes OpenCV, Firebase, and an ESP32-CAM to process video feeds and store detection data.

✨ Features

Real-time Detection: Uses YOLOv5 to detect people in live video streams.

Threshold-based Alarm System: Sends data to an Arduino via serial communication to trigger an alarm if the number of detected people exceeds a predefined limit.

ESP32-CAM Support: Captures and processes video frames from an ESP32-CAM.

Firebase Integration: Logs the number of detected people in a Firebase real-time database.

Color-Coded Bounding Boxes: Dynamically changes box colors based on the number of detected people.

🛠️ Technologies Used

Python

OpenCV (Computer Vision Processing)

YOLOv5 (Real-Time Object Detection)

PyTorch (Deep Learning Framework)

Firebase (Cloud Database)

ESP32-CAM (Video Streaming)

Arduino (Alarm Control)

📌 How It Works

Video Capture: The system captures frames from an ESP32-CAM or a connected camera.

Person Detection: YOLOv5 processes each frame to detect people.

Counting & Color-Coding:

<10 People: Green Boxes

10-19 People: Yellow Boxes

20-29 People: Red Boxes

Triggering Alarm:

The number of detected people is sent to an Arduino via serial communication.

If a predefined threshold is exceeded, an alarm is activated.

Firebase Logging: The count of detected people is stored in Firebase for monitoring.

🚀 Getting Started

🔧 Prerequisites

Ensure you have the following installed:

Python 3.x

OpenCV (pip install opencv-python)

PyTorch (pip install torch torchvision)

Firebase Admin SDK (pip install firebase-admin)

YOLOv5 (Clone from Ultralytics GitHub)

🔧 Installation

Clone the repository:

git clone https://github.com/yourusername/person-detection-yolo-arduino.git
cd person-detection-yolo-arduino

Set up Firebase:

Add your service account JSON file.

Update the database URL in the script.

Run the detection script:

python main.py

💡 Usage

Real-time monitoring: Detect people using an ESP32-CAM or USB camera.

Trigger alarm: Automatically alerts if overcrowding occurs.

Firebase Logging: Monitor people count remotely.

📅 Future Enhancements

Implement a web-based dashboard for monitoring.

Integrate edge AI with TensorRT for faster inference.

Deploy on Jetson Nano/Raspberry Pi for embedded applications.

💪 Contributing

Pull requests are welcome! Feel free to open issues for bug reports or feature requests.

📚 License

MIT License.
