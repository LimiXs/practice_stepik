#  https://stepik.org/lesson/701983/step/10?unit=702084
class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()}, {self.__ep.get_coords()}")


rect = Rectangle(0, 0, 20, 34)
