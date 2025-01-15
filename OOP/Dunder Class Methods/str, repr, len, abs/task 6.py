# https://stepik.org/lesson/701988/step/9?unit=702089
from math import sqrt


class RadiusVector:
    @staticmethod
    def validate_coords(values):
        return all(type(x) in (int, float) for x in values)

    def __init__(self, *args):
        if self.validate_coords(args):
            if len(args) == 1 and type(args[0]) == int:
                self.coords = [0] * args[0]
            else:
                self.coords = list(args)

    def set_coords(self, *args):
        if self.validate_coords(args):
            if len(args) == 1 and type(args[0]) == int:
                self.coords = [0] * args[0]
            else:
                for i in range(min(len(self.coords), len(args))):
                    self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        """
        вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N)
        корень квадратный из суммы квадратов координат
        """
        return sqrt(sum(x * x for x in self.coords))


vector3D = RadiusVector(3)

vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
print(a, b, c)

vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются

print(vector3D.get_coords())

vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
