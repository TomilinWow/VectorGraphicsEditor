class Selection:
    """
    Абстрактный класс селектор
    """

    def __init__(self, graf):
        self.grabbed = True
        self.graf = graf

    def draw(self, painter):
        pass

    def try_grab_marker(self, x, y):
        pass

    def try_release(self):
        pass

    def try_drag_to(self, x, y):
        pass

    def try_grab(self, x, y):
        if self.try_grab_marker(x, y):
            self.grab_x = x
            self.grab_y = y
            return True
        elif self.graf.in_body(x, y):
            self.grab_x = x
            self.grab_y = y
            self.drag = 0
            return True
        else:
            return False

    def set_point(self, x, y):
        self.grab_x = x
        self.grab_y = y


class FramedObjSelection(Selection):
    """
    Класс прямоугольного селектора объекта
    """

    def __init__(self, graf):
        super().__init__(graf)
        self.change_selection()
        self.drag = None

    def change_selection(self):
        """
        Смена координат слектора
        """
        self.x1 = self.graf.frame.x1
        self.y1 = self.graf.frame.y1
        self.x2 = self.graf.frame.x2
        self.y2 = self.graf.frame.y1
        self.x3 = self.graf.frame.x2
        self.y3 = self.graf.frame.y2
        self.x4 = self.graf.frame.x1
        self.y4 = self.graf.frame.y2

    def try_grab_marker(self, x, y):
        """
        Метод опредления захвата маркера фигуры
        :param x: координата x
        :param y: координата y
        """
        if self.x1 + 6 > x and self.x1 - 6 < x and self.y1 + 6 > y and self.y1 - 6 < y:
            self.drag = 1
            return True

        if self.x2 + 6 > x and self.x2 - 6 < x and self.y2 + 6 > y and self.y2 - 6 < y:
            self.drag = 2
            return True

        if self.x3 + 6 > x and self.x3 - 6 < x and self.y3 + 6 > y and self.y3 - 6 < y:
            self.drag = 3
            return True

        if self.x4 + 6 > x and self.x4 - 6 < x and self.y4 + 6 > y and self.y4 - 6 < y:
            self.drag = 4
            return True

    def try_drag_to(self, x, y):
        """
        Попытка перетаскивания маркера
        :param x: координата х при нажатии мышки
        :param y: координата y при нажатии мышки
        """
        dx = x - self.grab_x
        dy = y - self.grab_y
        self.graf.drag_state = True

        if self.drag == 0:
            self.graf.move(dx, dy)
        elif self.drag == 1:
            self.graf.move_first_marker(dx, dy)
        elif self.drag == 2:
            self.graf.move_second_marker(dx, dy)
        elif self.drag == 3:
            self.graf.move_third_marker(dx, dy)
        elif self.drag == 4:
            self.graf.move_fourth_marker(dx, dy)
        self.change_selection()

    def draw(self, painter):
        """
        Отрисовка селектора фигуры
        :param painter: средство отрисовки
        """
        painter.frame_selection(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)


class LineSelection(FramedObjSelection):
    """
    Класс селектора для линии
    """

    def __init__(self, graf):
        super().__init__(graf)
        self.change_selection()

    def change_selection(self):
        """
        Смена координат слектора
        """
        self.x1 = self.graf.frame.x1
        self.y1 = self.graf.frame.y1
        self.x2 = self.graf.frame.x2
        self.y2 = self.graf.frame.y2

    def try_drag_to(self, x, y):
        """
        Метод опредления захвата маркера линии
        :param x: координата x
        :param y: координата y
        """
        dx = x - self.grab_x
        dy = y - self.grab_y
        self.graf.drag_state = True
        if self.drag == 0:
            self.graf.move(dx, dy)
        elif self.drag == 1:
            self.graf.move_first_marker(dx, dy)
        elif self.drag == 3:
            self.graf.move_third_marker(dx, dy)
        self.change_selection()

    def try_grab_marker(self, x, y):
        """
        Попытка перетаскивания маркера линии
        :param x: координата х при нажатии мышки
        :param y: координата y при нажатии мышки
        """
        if self.x1 + 6 > x and self.x1 - 6 < x and self.y1 + 6 > y and self.y1 - 6 < y:
            self.drag = 1
            return True

        if self.x2 + 6 > x and self.x2 - 6 < x and self.y2 + 6 > y and self.y2 - 6 < y:
            self.drag = 3
            return True

    def draw(self, painter):
        """
        Отрисовка селектора линии
        :param painter: средство отрисовки
        """
        painter.line_selection(self.x1, self.y1, self.x2, self.y2)
