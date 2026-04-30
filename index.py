import cv2

# Load YOLO model (you need yolov5 or yolov8 installed)
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # lightweight model

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Obstacle Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


for r in results:
    for box in r.boxes:
        confidence = box.conf[0]

        if confidence > 0.6:
            print("⚠️ Obstacle Detected!")
