"""
https://stepik.org/lesson/701975/step/10?unit=702076
"""
from typing import List, Union


class Table:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, goods: List[Union[Table, TV, Notebook, Cup]] = None):
        self.goods = goods if goods is not None else []

    def add(self, gd: Union[Table, TV, Notebook, Cup]):
        self.goods.append(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{good.name}: {good.price}' for good in self.goods]


cart = Cart()
cart.add(TV('LG32', 32.4))
cart.add(TV('ASUSu7', 25))
cart.add(Table('woodik', 5.5))
cart.add(Notebook('ALIEN 5.0', 60))
cart.add(Notebook('MSI g12', 50.9))
cart.add(Cup('HL', 3))
