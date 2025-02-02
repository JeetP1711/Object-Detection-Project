from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
# Ama model ni details api che me and ema specify karyu che ke kayu model che and ama yolov8l means "YOLO Version 8 Model large", and avi ritna aa chalse
results = model("Images/2.png", show=True)
# Ama me jyare show=true lakhyu eno matlab ki aa mane image ma batavse ke su detect thayu che and kya detect thayu che and kevi ritna thayu che
cv2.waitKey(0)
# And ahiya cv2 waitkey no matlab ke aa wait karse and image mane batavse jya sudhi hu ene bandh na karu