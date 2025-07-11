import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 展示/输入框示例')
        self.resize(400, 300)

        # 垂直布局
        layout = QVBoxLayout()

        # 展示文本框（多行，只读）
        self.display_box = QTextEdit()
        self.display_box.setReadOnly(True)  # 只读

        # 输入文本框（单行）
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText('请输入内容，然后回车')

        # 输入框按下回车时，触发函数
        self.input_box.returnPressed.connect(self.append_text)

        # 把两个控件放到布局里
        layout.addWidget(self.display_box)
        layout.addWidget(self.input_box)

        self.setLayout(layout)

    def append_text(self):
        text = self.input_box.text().strip()
        if text:
            # 把输入的内容追加到展示框
            self.display_box.append(text)
            self.input_box.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ChatWindow()
    win.show()
    sys.exit(app.exec_())