#  https://stepik.org/lesson/701985/step/9?unit=702086
class FloatValue:
    """
    Это класс дескриптора
    """
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.cells = [[Cell() for j in range(M)] for i in range(N)]


start = 1.00
table = TableSheet(N=5, M=3)
for row in table.cells:
    for cell in row:
        cell.value = start
        start += 1.00

print(table.cells[-1][-1].value)
