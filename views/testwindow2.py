import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QListWidget, QListWidgetItem
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 界面示例：侧边栏 + 展示输入")
        self.resize(800, 500)

        # 主横向布局
        main_layout = QHBoxLayout()

        # 左侧：侧边栏（这里用 QListWidget 示范）
        self.sidebar = QListWidget()
        self.sidebar.addItem(QListWidgetItem("ChatGPT"))
        self.sidebar.addItem(QListWidgetItem("GPT"))
        self.sidebar.addItem(QListWidgetItem("Image Generator"))
        self.sidebar.addItem(QListWidgetItem("OCR"))
        self.sidebar.addItem(QListWidgetItem("Fine-Tune Guide"))

        # 右侧：垂直布局，上展示下输入
        right_layout = QVBoxLayout()

        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("请输入内容，按 Enter 发送")
        self.input_box.returnPressed.connect(self.append_text)

        right_layout.addWidget(self.display_box)
        right_layout.addWidget(self.input_box)

        # 把左右放进主布局
        main_layout.addWidget(self.sidebar, 1)      # 左侧栏，比例 1
        main_layout.addLayout(right_layout, 4)      # 右侧上下，比例 4

        self.setLayout(main_layout)

    def append_text(self):
        text = self.input_box.text().strip()
        if text:
            self.display_box.append(text)
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())