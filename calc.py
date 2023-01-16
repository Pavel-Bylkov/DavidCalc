from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from display import Display

class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

def press_num(num):
    if display.text() != "0":
        display.setText(display.text() + str(num))
    else:
        display.setText(str(num))

def num1():
    press_num(1)

def num2():
    press_num(2)

def num3():
    press_num(3)

def num4():
    press_num(4)

def num5():
    press_num(5)

def num6():
    press_num(6)

def num7():
    press_num(7)

def num8():
    press_num(8)

def num9():
    press_num(9)

def num0():
    press_num(0)

app = QApplication([])
win = QWidget()

win.setWindowTitle("Super Calculator")
win.resize(300, 400)

box = QVBoxLayout()  # для вертикального размещения виджетов

display = Display()  # подключаем свой
box.addWidget(display, alignment=Qt.AlignRight)

line = QHBoxLayout()  # для горизонтального размещения виджетов
btnPerc = MyButton("%")
line.addWidget(btnPerc)
btnCE = MyButton("CE")
line.addWidget(btnCE)
btnC = MyButton("C")
line.addWidget(btnC)
btnDel = MyButton("«")
line.addWidget(btnDel)

box.addLayout(line)

line2 = QHBoxLayout()  # для горизонтального размещения виджетов
btnreciprocal = MyButton("1÷x")
line2.addWidget(btnreciprocal)
btnx2 = MyButton("xª")
line2.addWidget(btnx2)
btnSQRT = MyButton("√")
line2.addWidget(btnSQRT)
btnDiv = MyButton("÷")
line2.addWidget(btnDiv)

box.addLayout(line2)

line3 = QHBoxLayout()  # для горизонтального размещения виджетов
btn7 = MyButton("7")
line3.addWidget(btn7)
btn8 = MyButton("8")
line3.addWidget(btn8)
btn9 = MyButton("9")
line3.addWidget(btn9)
btnX = MyButton("×")
line3.addWidget(btnX)

box.addLayout(line3)

line4 = QHBoxLayout()
btn4 = MyButton("4")
line4.addWidget(btn4)
btn5 = MyButton("5")
line4.addWidget(btn5)
btn6 = MyButton("6")
line4.addWidget(btn6)
btnmin = MyButton("-")
line4.addWidget(btnmin)

box.addLayout(line4)

line5 = QHBoxLayout()
btn1 = MyButton("1")
line5.addWidget(btn1)
btn2 = MyButton("2")
line5.addWidget(btn2)
btn3 = MyButton("3")
line5.addWidget(btn3)
btnplus = MyButton("+")
line5.addWidget(btnplus)

box.addLayout(line5)

line6 = QHBoxLayout()
btnposneg = MyButton("+/-")
line6.addWidget(btnposneg)
btn0 = MyButton("0")
line6.addWidget(btn0)
btndot= MyButton(".")
line6.addWidget(btndot)
btnequal = MyButton("=")
line6.addWidget(btnequal)


box.addLayout(line6)

win.setLayout(box)

# привязываем функции обработчики к кнопкам
btn1.clicked.connect(num1)
btn2.clicked.connect(num2)
btn3.clicked.connect(num3)
btn4.clicked.connect(num4)
btn5.clicked.connect(num5)
btn6.clicked.connect(num6)
btn7.clicked.connect(num7)
btn8.clicked.connect(num8)
btn9.clicked.connect(num9)
btn0.clicked.connect(num0)
win.show()
app.exec()
