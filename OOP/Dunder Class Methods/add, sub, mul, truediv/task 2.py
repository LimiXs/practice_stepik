# https://stepik.org/lesson/701989/step/7?unit=702090

class ListMath:
    def __init__(self, data: list = None):
        if data is None:
            self.lst_math = []
        else:
            self.lst_math = [x for x in data if type(x) in (int, float)]
        self.len_lst = len(self.lst_math)

    @staticmethod
    def validate_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Можно использовать только числа.")

    def __add__(self, other):
        self.validate_value(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        self.validate_value(other)
        return ListMath([other + x for x in self.lst_math])

    def __iadd__(self, other):
        self.validate_value(other)
        for i in range(self.len_lst):
            self.lst_math[i] += other

        return self

    def __sub__(self, other):
        self.validate_value(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        self.validate_value(other)
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.validate_value(other)
        for i in range(self.len_lst):
            self.lst_math[i] = self.lst_math[i] - other

        return self

    def __mul__(self, other):
        self.validate_value(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        self.validate_value(other)
        return ListMath([other * x for x in self.lst_math])

    def __imul__(self, other):
        self.validate_value(other)
        for i in range(self.len_lst):
            self.lst_math[i] *= other

        return self

    def __truediv__(self, other):
        self.validate_value(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        self.validate_value(other)
        return ListMath([other / x for x in self.lst_math])

    def __itruediv__(self, other):
        self.validate_value(other)
        for i in range(self.len_lst):
            self.lst_math[i] /= other

        return self


lst = ListMath([1, "abc", -5, 7.68, True])  # ListMath: [1, -5, 7.68]
print(lst.lst_math)
lst = lst + 76  # сложение каждого числа списка с определенным числом
print(lst.lst_math)
lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
print(lst.lst_math)
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.lst_math)
# lst = lst - 76  # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst  # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst  # деление числа на каждый элемент списка
# lst /= 13.0
