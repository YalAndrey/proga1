import sys

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
import random
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loadUi('UI.ui')
        self.bt = ''
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.bt = "Левая"
            self.repaint()
        elif (event.button() == Qt.RightButton):
            self.bt = "Правая"
            self.repaint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.bt = 'Пробел'
            self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        if self.bt == 'Правая':
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            num = random.randint(1, 400)
            qp.drawRect(int(self.x - num / 2), int(self.y - num / 2), num, num)
        elif self.bt == 'Левая':
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            num = random.randint(1, 400)
            qp.drawEllipse(int(self.x - num / 2), int(self.y - num / 2), num, num)
        elif self.bt == 'Пробел':
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            num = random.randint(1, 400)
            qp.drawPolygon(QPoint(self.x, int(self.y - num / 2)),
                           QPoint(int(self.x + num // 2), int(self.y + num // 2)),
                           QPoint(int(self.x - num // 2), int(self.y + num // 2)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())