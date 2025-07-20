import cv2
from ultralytics import YOLO
import time  # 加上这一行

# 加载YOLOv8预训练模型（第一次运行会自动下载）
model = YOLO("yolov8n.pt")  # 可选 yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 无法打开摄像头")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 读取失败")
        break

    time.sleep(1)  # 控制为每 0.2 秒一帧（约 5 FPS）
    # 推理：检测物体
    results = model(frame)[0]

    # 在图像上绘制检测框
    annotated_frame = results.plot()

    # print(results)
    # 显示图像
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
