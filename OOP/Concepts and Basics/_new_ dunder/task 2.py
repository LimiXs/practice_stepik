"""
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""


class SingletonFive:
    __names = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__names) < 5:
            obj = super().__new__(cls)
            cls.__names.append(obj)
        else:
            obj = cls.__names[4]
        return obj

    def __init__(self, name: str):
        self.name = name
