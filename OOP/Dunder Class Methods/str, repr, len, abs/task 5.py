# https://stepik.org/lesson/701988/step/8?unit=702089
from  math import sqrt


class Complex:
    def __init__(self, real: (float, int), img: (float, int)):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) not in (float, int):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) not in (float, int):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        """
        sqrt(real*real + img*img)
        """
        return  sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
