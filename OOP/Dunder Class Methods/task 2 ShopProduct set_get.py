#  https://stepik.org/lesson/701986/step/6?unit=702087
class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __init__(self,name, weight, price):
        self.id = Product.id + 1
        self.name = name
        self.weight = weight
        self.price = price

        Product.id = self.id

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        return super().__delattr__(item)

    def __setattr__(self, key, value):
        if key == "name":
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")

        if key == "weight" or key == "price":
            if not isinstance(value, (float, int)) or value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)
