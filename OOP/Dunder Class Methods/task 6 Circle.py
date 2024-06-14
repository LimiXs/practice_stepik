#  https://stepik.org/lesson/701986/step/10?unit=702087
class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def radius(self):
        return self.__radius

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):

            first_condition = key == "radius" and value > 0
            second_condition = key in ("x", "y")

            if first_condition or second_condition:
                object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
print(x, y, res)