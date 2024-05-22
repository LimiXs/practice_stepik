"""
https://stepik.org/lesson/701976/step/11?unit=702077
"""


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def clone(self):
        return Point(self._x, self._y)


x, y = 5, 6

pt = Point(x, y)
pt_clone = pt.clone()
