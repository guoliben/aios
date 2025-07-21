from paddleocr import PaddleOCR
# ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 中文模型
ocr = PaddleOCR(use_angle_cls=True, lang='ch', use_paddle_predict=False)
# # result = ocr.ocr('testocr.jpg')
#
# # for line in result[0]:
# #     print(line[1][0])  # 输出文字
# #
# ocr = PaddleOCR(
#     use_angle_cls=True,
#     lang='ch',
#     det_model_dir='./models/det',
#     rec_model_dir='./models/rec',
#     cls_model_dir='./models/cls'
# )