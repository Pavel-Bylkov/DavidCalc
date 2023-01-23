from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from display import Display

operation = ""
first_number = 0


class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

class MyWin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        f = key_pressed.get(event.key(), None)
        if f is not None:
            f()
        event.accept()

def press_num(num):
    if display.text() != "0":
        display.setText(display.text() + str(num))
    else:
        display.setText(str(num))


def all_clear():
    global operation, first_number
    display.setText("0")
    operation = ""
    first_number = 0

def add():
    global operation, first_number
    first_number = float(display.text())
    operation = "+"
    display.setText("0")

def minus():
    global operation, first_number
    first_number = float(display.text())
    operation = "-"
    display.setText("0")

def mult():
    global operation, first_number
    first_number = float(display.text())
    operation = "×"
    display.setText("0")

def div():
    global operation, first_number
    first_number = float(display.text())
    operation = "÷"
    display.setText("0")

def power():
    global operation, first_number
    first_number = float(display.text())
    operation = "p"
    display.setText("0")

def posneg():
    global operation, first_number
    first_number = float(display.text())
    result = -1 * first_number
    display.setText(str(result))

def recip():
    global operation, first_number
    first_number = float(display.text())
    result = 1 / first_number
    display.setText(str(result))

def equal():
    result = 0
    if operation == "+":
        result = first_number + float(display.text())
    elif operation == "-":
        result = first_number - float(display.text())
    elif operation == "×":
        result = first_number * float(display.text())
    elif operation == "÷":
        result = first_number / float(display.text())
    elif operation == "p":
        result = first_number ** float(display.text())
    display.setText(str(result))

key_pressed = {Qt.Key_0: lambda: press_num(0),
               Qt.Key_1: lambda: press_num(1),
               Qt.Key_2: lambda: press_num(2),
               Qt.Key_3: lambda: press_num(3),
               Qt.Key_4: lambda: press_num(4),
               Qt.Key_5: lambda: press_num(5),
               Qt.Key_6: lambda: press_num(6),
               Qt.Key_7: lambda: press_num(7),
               Qt.Key_division: div,
               Qt.Key_Plus: add}

app = QApplication([])
win = MyWin()

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
btn1.clicked.connect(lambda: press_num(1))
btn2.clicked.connect(lambda: press_num(2))
btn3.clicked.connect(lambda: press_num(3))
btn4.clicked.connect(lambda: press_num(4))
btn5.clicked.connect(lambda: press_num(5))
btn6.clicked.connect(lambda: press_num(6))
btn7.clicked.connect(lambda: press_num(7))
btn8.clicked.connect(lambda: press_num(8))
btn9.clicked.connect(lambda: press_num(9))
btn0.clicked.connect(lambda: press_num(0))

btnC.clicked.connect(all_clear)
btnplus.clicked.connect(add)
btnequal.clicked.connect(equal)
btnmin.clicked.connect(minus)
btnX.clicked.connect(mult)
btnDiv.clicked.connect(div)
btnx2.clicked.connect(power)
btnposneg.clicked.connect(posneg)
btnreciprocal.clicked.connect(recip)

win.show()
app.exec()
