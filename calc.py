from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setWindowTitle("Super Calculator")
win.resize(300, 400)

box = QVBoxLayout()  # для вертикального размещения виджетов

display = QLabel("0123456789")
box.addWidget(display, alignment=Qt.AlignRight)

line = QHBoxLayout()  # для горизонтального размещения виджетов
btn1 = QPushButton("1")
line.addWidget(btn1)
btn2 = QPushButton("2")
line.addWidget(btn2)
btn3 = QPushButton("3")
line.addWidget(btn3)

box.addLayout(line)

win.setLayout(box)

win.show()
app.exec()
