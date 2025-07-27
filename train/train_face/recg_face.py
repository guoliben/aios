import cv2
import os

net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")


filepath = "dataset/face/"
for filename in os.listdir(filepath):
    print(filename)
    filename = os.path.join(filepath, filename)
    img = cv2.imread(filename)
    (h, w) = img.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    has_face = any(d[2] > 0.5 for d in detections[0, 0])

    print("有人脸" if has_face else "无人脸")