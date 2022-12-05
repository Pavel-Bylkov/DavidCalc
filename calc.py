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
btnPerc = QPushButton("%")
line.addWidget(btnPerc)
btnCE = QPushButton("CE")
line.addWidget(btnCE)
btnC = QPushButton("C")
line.addWidget(btnC)
btnDel = QPushButton("<")
line.addWidget(btnDel)

box.addLayout(line)

line2 = QHBoxLayout()  # для горизонтального размещения виджетов
btn1x = QPushButton("1/x")
line2.addWidget(btn1x)
btnx2 = QPushButton("x2")
line2.addWidget(btnx2)
btnSQRT = QPushButton("xv2")
line2.addWidget(btnSQRT)
btnDiv = QPushButton("/")
line2.addWidget(btnDiv)

box.addLayout(line2)

line3 = QHBoxLayout()  # для горизонтального размещения виджетов
btn1 = QPushButton("1")
line3.addWidget(btn1)
btn2 = QPushButton("2")
line3.addWidget(btn2)
btn3 = QPushButton("3")
line3.addWidget(btn3)

box.addLayout(line3)

win.setLayout(box)

win.show()
app.exec()
