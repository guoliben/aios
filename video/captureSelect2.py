import cv2
from ultralytics import YOLO
import time

# 加载YOLOv8n模型
model = YOLO("yolov8n.pt")

# 打开摄像头（你可以改为 cap = cv2.VideoCapture(0)）
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ 无法打开摄像头")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 读取失败")
        break

    # 推理：检测物体
    results = model(frame)[0]

    # 遍历检测结果，打印每个物体
    for box in results.boxes:
        cls_id = int(box.cls[0])  # 类别ID
        conf = float(box.conf[0])  # 置信度
        xyxy = box.xyxy[0].tolist()  # 边界框坐标
        label = model.names[cls_id]  # 类别名称

        print(f"检测到: {label} - 置信度: {conf:.2f}, 坐标: {xyxy}")

    # 在图像上绘制检测框
    annotated_frame = results.plot()

    # 显示图像
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)  # 可调节帧率，减轻CPU/GPU负担

cap.release()
cv2.destroyAllWindows()
