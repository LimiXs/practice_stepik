class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __getattr__(self, name):
        if name in {'a', 'b', 'c'}:
            return self.__dict__[f'_{self.__class__.__name__}__{name}']
        raise AttributeError(f"'Такого объекта не существует '{name}'")

    def __setattr__(self, name, value):
        if name in {'a', 'b', 'c'}:
            if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
                self.__dict__[f'_{self.__class__.__name__}__{name}'] = value
        else:
            super().__setattr__(name, value)

    def __ge__(self, other):
        return self.a * self.b * self.c >= other.a * other.b * other.c

    def __gt__(self, other):
        return self.a * self.b * self.c > other.a * other.b * other.c

class ShopItem:
    def __init__(self, name: str, price: (int, float), dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [
    ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
    ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
    ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
    ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
