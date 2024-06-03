#  https://stepik.org/lesson/701984/step/9?unit=702085
class RadiusVector2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y