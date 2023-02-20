#подключаем модуль с направляющими линиями
from PyQt6.QtCore import Qt
#подключаем необходимые виджеты
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout,
                               QScrollArea)
from PyQt6.QtGui import QFont

# class for scrollable label
class Display(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)
        self.setFixedWidth(390)
        self.setFixedHeight(90)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)
        self.label.setFont(QFont('Arial', 24))
        self.label.setText("0")

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        # making label multi-line
        # self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

    def text(self):
        return self.label.text()