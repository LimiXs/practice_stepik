class ListMath:
    def __init__(self, data: list = None):
        if data is None:
            self.lst_math = []
        else:
            self.lst_math = [x for x in data if type(x) in (int, float)]
        self.len_lst = len(self.lst_math)

    def __add__(self, other):
        if type(other) is (int, float):
            return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        if type(other) is (int, float):
            return ListMath([other + x for x in self.lst_math])

    def __iadd__(self, other):
        if type(other) is (int, float):
            for i in range(self.len_lst):
                self.lst_math[i] += other

    def __sub__(self, other):
        if type(other) is (int, float):
            return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        if type(other) is (int, float):
            return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        if type(other) is (int, float):
            for i in range(self.len_lst):
                self.lst_math[i] -= other

    def __mul__(self, other):
        if type(other) is (int, float):
            return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        if type(other) is (int, float):
            return ListMath([other * x for x in self.lst_math])

    def __imul__(self, other):
        if type(other) is (int, float):
            for i in range(self.len_lst):
                self.lst_math[i] *= other

    def __truediv__(self, other):
        if type(other) is (int, float):
            return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        if type(other) is (int, float):
            return ListMath([other / x for x in self.lst_math])

    def __itruediv__(self, other):
        if type(other) is (int, float):
            for i in range(self.len_lst):
                self.lst_math[i] /= other


lst = ListMath([1, 2, 3, 4, 5])
print("Исходный список:", lst.lst_math)

lst2 = lst + 10
print("После сложения с 10:", lst2.lst_math)

lst3 = 10 + lst
print("После сложения с 10 (обратное):", lst3.lst_math)

lst -= 2
print("После вычитания 2 (ин-место):", lst.lst_math)

lst4 = lst * 3
print("После умножения на 3:", lst4.lst_math)

lst5 = 3 * lst
print("После умножения на 3 (обратное):", lst5.lst_math)

lst2 = ListMath([1, 2, 3, 4, 5])
lst2 /= 2
print("После деления на 2 (ин-место):", lst.lst_math)

lst6 = 10 / lst
print("После деления 10 на список:", lst6.lst_math)