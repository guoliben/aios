import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QListWidget, QListWidgetItem, QLabel
)
from PyQt5.QtGui import QMovie, QRegion
from PyQt5.QtCore import Qt, QRect


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 圆形 GIF 浮层示例")
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

        # 右侧：上下布局
        right_layout = QVBoxLayout()

        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("请输入内容，按 Enter 发送")
        self.input_box.returnPressed.connect(self.append_text)

        right_layout.addWidget(self.display_box)
        right_layout.addWidget(self.input_box)

        # 把右侧布局放到 QWidget，用作浮层的 parent
        self.right_widget = QWidget()
        self.right_widget.setLayout(right_layout)

        # 左右放进主布局
        main_layout.addWidget(self.sidebar, 1)
        main_layout.addWidget(self.right_widget, 4)
        self.setLayout(main_layout)

        # ============ 新增：右侧叠加一个圆形 GIF 浮层 ============
        self.overlay_label = QLabel(self.right_widget)
        self.overlay_label.setAttribute(Qt.WA_TranslucentBackground)

        # 设置位置和大小（正方形，才能裁成圆形）
        x, y, w, h = 250, 250, 60, 60
        self.overlay_label.setGeometry(x, y, w, h)

        # 加载 GIF
        # 替换成你的 GIF 路径，最好放到同一目录
        gif_path = os.path.join(os.path.dirname(__file__), "../voice.gif")
        self.movie = QMovie(gif_path)
        self.overlay_label.setMovie(self.movie)
        self.movie.start()

        # 用 QRegion 裁剪成圆形
        rect = QRect(0, 0, w, h)
        region = QRegion(rect, QRegion.Ellipse)
        self.overlay_label.setMask(region)

        # 保证浮层在最前
        self.overlay_label.raise_()

    def append_text(self):
        text = self.input_box.text().strip()
        if text:
            self.display_box.append(f'<p align="right">{text}</p>')
            self.input_box.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
