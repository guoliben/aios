# pip install ultralytics
# pip install paddleocr
# pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/paddle_cpu.html


import cv2
from ultralytics import YOLO
from paddleocr import PaddleOCR

# 初始化 YOLO 模型（这里用 yolov8n，自行替换更强的模型）
model = YOLO("yolov8n.pt")

# 初始化 OCR（中文 + 方向分类）
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# 加载图像（可替换为摄像头帧）
image_path = 'your_image.jpg'
image = cv2.imread(image_path)

# 使用 YOLO 检测图像中的物体
results = model(image)[0]

# 遍历检测框，筛选出可能的文本区域（可根据类别或大小筛选）
for box in results.boxes:
    xyxy = box.xyxy[0].cpu().numpy().astype(int)  # 坐标：左上右下
    x1, y1, x2, y2 = xyxy
    crop = image[y1:y2, x1:x2]  # 截取区域

    # 用 OCR 对该区域识别
    ocr_result = ocr.ocr(crop, cls=True)

    # 打印识别结果
    for line in ocr_result:
        for word_info in line:
            text = word_info[1][0]
            score = word_info[1][1]
            print(f"📄 文本: {text}, 置信度: {score:.2f}")

    # 可选：画框
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示带框图像
cv2.imshow("YOLO + OCR", image)
cv2.waitKey(0)
cv2.destroyAllWindows()