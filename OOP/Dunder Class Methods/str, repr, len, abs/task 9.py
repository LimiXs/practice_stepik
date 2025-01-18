# https://stepik.org/lesson/701988/step/12?unit=702089

class PolyLine:
    def __init__(self, start_coord: tuple, *args):
        self.points = []
        self.points.append(start_coord)
        self.points.extend(args)

    def add_coord(self, x, y):
        self.points.append((x, y))

    def remove_coord(self, indx):
        self.points.pop(indx)

    def get_coords(self):
        return self.points
