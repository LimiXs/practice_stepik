#  https://stepik.org/lesson/701984/step/9?unit=702085
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self._validate_coordinate(x)
        self.__y = self._validate_coordinate(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = self._validate_coordinate(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = self._validate_coordinate(value)

    def _validate_coordinate(self, value):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            return value
        return 0

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2
