import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QListWidget, QListWidgetItem, QLabel
)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect

import os

def append_text(self):
    text = self.input_box.text().strip()
    if text:
        # 使用 HTML，让文本右对齐
        self.display_box.append(f'<p align="right">{text}</p>')
        self.input_box.clear()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 界面示例：浮层 + 动态图片")
        self.resize(800, 500)

        # 主横向布局
        main_layout = QHBoxLayout()

        # 左侧：侧边栏
        self.sidebar = QListWidget()
        self.sidebar.addItem(QListWidgetItem("ChatGPT"))
        self.sidebar.addItem(QListWidgetItem("GPT"))
        self.sidebar.addItem(QListWidgetItem("Image Generator"))
        self.sidebar.addItem(QListWidgetItem("OCR"))
        self.sidebar.addItem(QListWidgetItem("Fine-Tune Guide"))

        # 右侧：垂直布局
        right_layout = QVBoxLayout()

        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("请输入内容，按 Enter 发送")
        self.input_box.returnPressed.connect(self.append_text)

        right_layout.addWidget(self.display_box)
        right_layout.addWidget(self.input_box)

        # 把左右放进主布局
        main_layout.addWidget(self.sidebar, 1)
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        main_layout.addWidget(right_widget, 4)

        self.setLayout(main_layout)

        # =============== 新增：浮层放 GIF ===============
        self.overlay_label = QLabel(right_widget)
        self.overlay_label.setAttribute(Qt.WA_TranslucentBackground)
        self.overlay_label.setGeometry(300, 100, 100, 100)  # (x, y, w, h)

        # 加载 GIF
        gif_path = os.path.join(os.path.dirname(__file__), '..', 'voice.gif')
        self.movie = QMovie(gif_path)
        self.overlay_label.setMovie(self.movie)
        self.movie.start()

        # 用 QRegion 把 QLabel 裁成圆形
        rect = QRect(0, 0, w, h)
        region = QRegion(rect, QRegion.Ellipse)
        self.overlay_label.setMask(region)

        # 保证浮层在最上层
        self.overlay_label.raise_()

        # 层叠显示在最前
        self.overlay_label.raise_()

    def append_text(self):
        text = self.input_box.text().strip()
        if text:
            # self.display_box.append(text)
            self.display_box.append(f'<p align="right">{text}</p>')
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())