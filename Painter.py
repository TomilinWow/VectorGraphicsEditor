from PyQt5.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen
from PyQt5 import QtGui, Qt

class Painter:
    """
    Класс отрисовщик
    """
    def __init__(self):
        super().__init__()
        self.pen_color = QtGui.QColor("green")
        self.pen_width = 1
        self.brush_color = QtGui.QColor("green")

    def set_port(self, x0, y0, w, h, painter):
        self.painter = painter
        self.x0 = x0
        self.y0 = y0
        self.w = w
        self.h = h

    def line(self, x1, y1, x2, y2):
        pen = QPen(self.pen_color, self.pen_width)
        self.painter.addLine(x1, y1, x2, y2, pen)

    def rect(self, x1, y1, x2, y2):
        """
        Определение координат прямоугольника
        """
        xmax = max(x1, x2)
        xmin = min(x1, x2)
        ymax = max(y1, y2)
        ymin = min(y1, y2)
        w = xmax - xmin
        h = ymax - ymin

        pen = QPen(self.pen_color, self.pen_width)
        self.painter.addRect(xmin, ymin, w, h, pen, self.brush_color)

    def ellipse(self, x1, y1, x2, y2):
        """
        Определение координат эллипса
        """
        xmax = max(x1, x2)
        xmin = min(x1, x2)
        ymax = max(y1, y2)
        ymin = min(y1, y2)
        w = xmax - xmin
        h = ymax - ymin

        pen = QPen(self.pen_color, self.pen_width)
        self.painter.addEllipse(xmin, ymin, w, h, pen, self.brush_color)

    def frame_selection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        #маркеры
        pen = QPen(QtGui.QColor("black"), 1)
        self.painter.addRect(x1 - 4, y1 - 4, 8, 8, pen)
        self.painter.addRect(x2 - 4, y2 - 4, 8, 8, pen)
        self.painter.addRect(x3 - 4, y3 - 4, 8, 8, pen)
        self.painter.addRect(x4 - 4, y4 - 4, 8, 8, pen)

        #контур выделения
        xmax = max(x1, x3)
        xmin = min(x1, x3)
        ymax = max(y1, y3)
        ymin = min(y1, y3)
        w = xmax - xmin
        h = ymax - ymin
        self.painter.addRect(xmin, ymin, w, h, pen)


    def line_selection(self, x1, y1, x2, y2):
        # маркеры
        pen = QPen(QtGui.QColor("black"), 1)
        self.painter.addRect(x1 - 4, y1 - 4, 8, 8, pen)
        self.painter.addRect(x2 - 4, y2 - 4, 8, 8, pen)


    def clear(self):
        self.painter.clear()
