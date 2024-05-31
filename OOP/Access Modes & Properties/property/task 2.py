#  https://stepik.org/lesson/701984/step/7?unit=702085
class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")
