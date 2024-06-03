#  https://stepik.org/lesson/701984/step/7?unit=702085
class WindowDlg:
    MIN_VALUE = 0
    MAX_VALUE = 10000

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if WindowDlg.check_range(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if WindowDlg.check_range(height):
            self.__height = height
            self.show()

    @classmethod
    def check_range(cls, value):
        return cls.MIN_VALUE <= value <= cls.MAX_VALUE
