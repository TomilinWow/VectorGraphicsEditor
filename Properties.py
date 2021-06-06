from PyQt5 import QtGui

class Properties:
    """
    Класс свойств
    """
    def __init__(self):
        self.prop_group = PropGroup()

    def apply_props(self, painter):
        for prop in self.prop_group.list_prop:
            prop.apply_props(painter)

class PropGroup:
    """
    Абстрактный класс свойств
    """
    def __init__(self):
        self.list_prop = []

    def apply_props(self, painter):
        pass

class PenProps(PropGroup):
    """
    Класс свойств ручки
    """
    def __init__(self, pen_color, pen_width):
        super().__init__()
        self.pen_color = pen_color
        self.pen_width = pen_width

    def apply_props(self, painter):
        """
        Перезаписываем применение всех свойств к Painter'у для ручки
        :param painter: класс Painter
        """
        painter.pen_color = self.pen_color
        painter.pen_width = self.pen_width


class BrushProps(PropGroup):
    """
    Класс свойств кисти
    """
    def __init__(self, brush_prop):
        super().__init__()
        self.brush_prop = brush_prop

    def apply_props(self, painter):
        """
        Перезаписываем применение всех свойств к Painter'у для кисти
        :param painter: класс Painter
        """
        painter.brush_color = self.brush_prop
