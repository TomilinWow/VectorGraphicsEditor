import GrafObject
from Selection import FramedObjSelection, LineSelection
import math


class Line(GrafObject.Figure):
    """
    Класс фигуры - Линия
    """

    def __init__(self, frame, props):
        super().__init__(frame, props)

    def draw_geometry(self, painter):
        """
        Отрисовка линии
        :param painter: средство рисования
        """
        painter.line(self.frame.x1, self.frame.y1, self.frame.x2, self.frame.y2)

    def in_body(self, x, y):
        """
        Определение попадания точки на линию
        :param x: координата x
        :param y: координата y
        """
        xmax = max(self.frame.x1, self.frame.x2)
        xmin = min(self.frame.x1, self.frame.x2)
        ymax = max(self.frame.y1, self.frame.y2)
        ymin = min(self.frame.y1, self.frame.y2)

        distance = abs((ymax - ymin) * x - (xmax - xmin) * y + xmax * ymin - ymax * xmin) / (
            math.sqrt(pow(ymax - ymin, 2) + pow(xmax - xmin, 2)))

        if xmin - 5 <= x and ymin - 5 <= y and xmax + 5 >= x and ymax + 5 >= y and distance < 5:
            return True
        else:
            return False

    def create_selection(self):
        """
        Создание селектора линии
        """
        return LineSelection(self)


class Rectangle(GrafObject.Figure):
    """
    Класс фигуры - Прямоугольник
    """

    def __init__(self, frame, props):
        super().__init__(frame, props)

    def draw_geometry(self, painter):
        """
        Отрисовка прямоугольника
        :param painter: средство рисования
        """
        painter.rect(self.frame.x1, self.frame.y1, self.frame.x2, self.frame.y2)

    def create_selection(self):
        """
        Создание селектора прямоугольника
        """
        return FramedObjSelection(self)

    def in_body(self, x, y):
        """
        Определение попадания точки в прямоугольник
        :param x: координата x
        :param y: координата y
        """
        xmax = max(self.frame.x1, self.frame.x2)
        xmin = min(self.frame.x1, self.frame.x2)
        ymax = max(self.frame.y1, self.frame.y2)
        ymin = min(self.frame.y1, self.frame.y2)
        w = xmax - xmin
        h = ymax - ymin

        if x > xmin and x < xmin + w and y > ymin and y < ymin + h:
            return True
        else:
            return False


class Ellipse(GrafObject.Figure):
    """
    Класс фигуры - Эллипс
    """

    def __init__(self, frame, props):
        super().__init__(frame, props)

    def draw_geometry(self, painter):
        """
        Отрисовка эллипса
        :param painter: средство рисования
        """
        painter.ellipse(self.frame.x1, self.frame.y1, self.frame.x2, self.frame.y2)

    def create_selection(self):
        """
        Создание селектора для эллипса
        """
        return FramedObjSelection(self)

    def in_body(self, x, y):
        """
        Определение попадания точки в эллипс
        :param x: координата x
        :param y: координата y
        """
        x_c = (self.frame.x1 + self.frame.x2) / 2
        y_c = (self.frame.y1 + self.frame.y2) / 2

        if pow(x - x_c, 2) / pow((self.frame.x2 - self.frame.x1) / 2, 2) + pow(y - y_c, 2) / pow(
                (self.frame.y2 - self.frame.y1) / 2, 2) <= 1:
            return True
        else:
            return False
