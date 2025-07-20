import cv2
import time

# 打开默认摄像头（0为默认）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 无法打开摄像头")
    exit()

print("📷 摄像头已开启，按空格键拍照，按 Esc 退出")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ 读取失败")
        break

    # 显示图像
    cv2.imshow('Camera', frame)

    # 等待键盘输入
    key = cv2.waitKey(1)
    if key == 27:  # Esc 键退出
        break
    elif key == 32:  # 空格键拍照
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"photo_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"✅ 已保存照片：{filename}")

# 释放资源
cap.release()
cv2.destroyAllWindows()
