import cv2
from ultralytics import YOLO
import pyttsx3
import time

# 初始化语音引擎
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 设置语速，可选调

# 加载 YOLOv8n 模型
model = YOLO("yolov8n.pt")

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 无法打开摄像头")
    exit()

last_labels = set()  # 上一次播报的类别，避免重复朗读

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 读取失败")
        break

    results = model(frame)[0]
    current_labels = set()

    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        label = model.names[cls_id]
        current_labels.add(label)

        print(f"检测到: {label} - 置信度: {conf:.2f}, 坐标: {xyxy}")

    # 找出新检测到的类别，进行语音播报
    new_labels = current_labels - last_labels
    for label in new_labels:
        engine.say(f"{label}")
    if new_labels:
        engine.runAndWait()

    last_labels = current_labels

    # 显示画面
    annotated_frame = results.plot()
    cv2.imshow("YOLOv8 实时目标识别", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.2)  # 控制频率，避免语音过快播报

cap.release()
cv2.destroyAllWindows()
