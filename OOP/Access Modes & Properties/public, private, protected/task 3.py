#  https://stepik.org/lesson/701983/step/8?unit=702084
class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
