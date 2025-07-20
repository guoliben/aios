import cv2
from ultralytics import YOLO

# 加载 YOLOv8s 模型（自动下载 yolov8n.pt）
model = YOLO("yolov8n.pt")

# 打开摄像头，0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 使用 YOLO 模型进行预测
    results = model(frame)

    # 处理检测结果
    for result in results:
        boxes = result.boxes  # 获取检测框
        for box in boxes:
            cls_id = int(box.cls[0])             # 类别 ID
            conf = float(box.conf[0])            # 置信度
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 边框坐标

            # 获取类别名称
            label = model.names[cls_id]
            label_text = f"{label} {conf:.2f}"

            # 画框和标签
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label_text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 显示结果
    cv2.imshow("YOLOv8s Real-time Detection", frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()