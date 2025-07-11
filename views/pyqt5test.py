import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Hello macOS App')

layout = QVBoxLayout()
layout.addWidget(QLabel('你好，这是一个 PyQt5 窗口！'))

window.setLayout(layout)
window.show()

sys.exit(app.exec_())