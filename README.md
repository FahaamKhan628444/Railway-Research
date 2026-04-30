# Railway-Research
Review of the obstacle detection on the railway tracks for the safety of the local pilots


# All-Weather Obstacle Detection System (Prototype)

##  Overview
This project demonstrates a basic prototype of an **Obstacle Detection System** using computer vision and deep learning techniques. The system uses a YOLO (You Only Look Once) model to detect objects in real-time through a webcam feed.

This implementation is a **demo prototype** inspired by the research topic:
> *“All-Weather Obstacle Alert System for Railway Loco Pilot Safety”*

---

##  Features
- Real-time object detection using YOLO
- Detects common obstacles such as:
  - Humans
  - Vehicles
  - Animals
- Displays bounding boxes with labels and confidence scores
- Prints alert message when an obstacle is detected
- Lightweight and easy to run

---

##  Tech Stack
- Python
- OpenCV
- YOLO (Ultralytics)
- NumPy

---

##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/obstacle-detection.git
cd obstacle-detection


pip install opencv-python ultralytics
