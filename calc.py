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
btnDel = QPushButton("«")
line.addWidget(btnDel)

box.addLayout(line)

line2 = QHBoxLayout()  # для горизонтального размещения виджетов
btnreciprocal = QPushButton("1÷x")
line2.addWidget(btnreciprocal)
btnx2 = QPushButton("xª")
line2.addWidget(btnx2)
btnSQRT = QPushButton("√")
line2.addWidget(btnSQRT)
btnDiv = QPushButton("÷")
line2.addWidget(btnDiv)

box.addLayout(line2)

line3 = QHBoxLayout()  # для горизонтального размещения виджетов
btn7 = QPushButton("7")
line3.addWidget(btn7)
btn8 = QPushButton("8")
line3.addWidget(btn8)
btn9 = QPushButton("9")
line3.addWidget(btn9)
btnX = QPushButton("×")
line3.addWidget(btnX)

box.addLayout(line3)

line4 = QHBoxLayout()
btn4 = QPushButton("4")
line4.addWidget(btn4)
btn5 = QPushButton("5")
line4.addWidget(btn5)
btn6 = QPushButton("6")
line4.addWidget(btn6)
btnmin = QPushButton("-")
line4.addWidget(btnmin)

box.addLayout(line4)

line5 = QHBoxLayout()
btn1 = QPushButton("1")
line5.addWidget(btn1)
btn2 = QPushButton("2")
line5.addWidget(btn2)
btn3 = QPushButton("3")
line5.addWidget(btn3)
btnplus = QPushButton("+")
line5.addWidget(btnplus)

box.addLayout(line5)

line6 = QHBoxLayout()
btnposneg = QPushButton("+/-")
line6.addWidget(btnposneg)
btn0 = QPushButton("0")
line6.addWidget(btn0)
btndot= QPushButton(".")
line6.addWidget(btndot)
btnequal = QPushButton("=")
line6.addWidget(btnequal)


box.addLayout(line6)

win.setLayout(box)

win.show()
app.exec()
