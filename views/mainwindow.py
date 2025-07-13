# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from PySide6.QtGui import QMovie, QRegion
from PySide6.QtCore import QRect
# from ui_mainwindow import Ui_MainWindow  # 用 pyside6-uic 生成的

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # === 新增: 用 QMovie 加载 GIF ===
        self.movie = QMovie("voice.gif")  # 换成你的路径
        self.ui.gifLabel.setMovie(self.movie)
        self.movie.start()

        # 用 QRegion 把 QLabel 裁成圆形
        rect = QRect(0, 0, 80, 80)
        region = QRegion(rect, QRegion.Ellipse)
        self.ui.gifLabel.setMask(region)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

#
# import sys
#
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtGui import QMovie, QRegion
# from PySide6.QtCore import QRect, Qt
#
# from ui_form import Ui_MainWindow
#
#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # === 用 QMovie 加载 GIF ===
#         self.movie = QMovie("voice.gif")  # 换成你的路径
#         self.ui.gifLabel.setMovie(self.movie)
#         self.movie.start()
#
#         # 圆形遮罩（可选）
#         rect = QRect(0, 0, 80, 80)
#         region = QRegion(rect, QRegion.Ellipse)
#         self.ui.gifLabel.setMask(region)
#
#         # === 输入框回车绑定 ===
#         # 给输入框绑定事件
#         self.ui.plainTextEdit.installEventFilter(self)
#
#         # 可选：显示区域（这里把 gifLabel 当显示区域不太合适，推荐另放 QLabel）
#         # 这里演示就直接改它的 Text
#         self.ui.gifLabel.setText("")
#
#     def eventFilter(self, watched, event):
#         if watched == self.ui.plainTextEdit and event.type() == event.KeyPress:
#             if event.key() in (Qt.Key_Return, Qt.Key_Enter):
#                 self.on_enter_pressed()
#                 return True
#         return super().eventFilter(watched, event)
#
#     def on_enter_pressed(self):
#         text = self.ui.plainTextEdit.toPlainText()
#         # 展示到 gifLabel
#         self.ui.gifLabel.setText(text)
#         # 可选：清空输入框
#         self.ui.plainTextEdit.clear()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = MainWindow()
#     widget.show()
#     sys.exit(app.exec())