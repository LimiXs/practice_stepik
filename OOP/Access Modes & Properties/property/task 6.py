#  https://stepik.org/lesson/701984/step/11?unit=702085
from math import sqrt, pow


class PathLines:

    def __init__(self, *args):
        self.lines = list((LineTo(0, 0), ) + args)

    def get_path(self):
        return self.lines[1:]

    def get_length(self):
        """
        L = sqrt((x1-x0)^2 + (y1-y0)^2)
        """
        last_x, last_y, summ_path = 0, 0, 0
        for elm in self.get_path():

            summ_path += sqrt(pow(elm.x - last_x, 2) + pow(elm.y - last_y, 2))
            last_x, last_y = elm.x, elm.y

        return summ_path

    def add_line(self, line):
        self.lines.append(line)


class LineTo:
    def __init__(self, x=0, y=0):  # (1, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
