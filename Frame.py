class Frame:
    """
    Класс области фигуры (фрейм фигуры)
    """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def combine(self, list):
        """
        Метод формирования общего фрейма фигур
        :param list: список фигур
        """
        for object in list:

            x1 = self.x1
            y1 = self.y1
            x2 = self.x2
            y2 = self.y2

            self.x1 = min(min(x1, x2), min(object.frame.x1, object.frame.x2))
            self.y1 = min(min(y1, y2), min(object.frame.y1, object.frame.y2))
            self.x2 = max(max(x1, x2), max(object.frame.x1, object.frame.x2))
            self.y2 = max(max(y1, y2), max(object.frame.y1, object.frame.y2))

    def move(self, x, y):
        """
        Смещение координат
        :param x: координата х
        :param y: координата y
        """
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y

    def move_first_marker(self, x, y):
        """
        Смещение первого маркера фигуры
        :param x: координата х
        :param y: координата y
        """
        self.x1 += x
        self.y1 += y

    def move_second_marker(self, x, y):
        """
        Смещение второго маркера фигуры
        :param x: координата х
        :param y: координата y
        """
        self.x2 += x
        self.y1 += y

    def move_third_marker(self, x, y):
        """
        Смещение третьего маркера фигуры
        :param x: координата х
        :param y: координата y
        """
        self.x2 += x
        self.y2 += y

    def move_fourth_marker(self, x, y):
        """
        Смещение четвертого маркера фигуры
        :param x: координата х
        :param y: координата y
        """
        self.x1 += x
        self.y2 += y
