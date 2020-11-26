from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
import random
import sys
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, e):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawRectangle()
        self.qp.end()

    def drawRectangle(self):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        self.qp.setPen(col)

        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.setBrush(QColor(random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255)))
        num = random.randint(1, 400)
        self.qp.drawEllipse(100, 100, num, num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())