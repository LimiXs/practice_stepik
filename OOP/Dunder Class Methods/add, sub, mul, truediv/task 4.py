# https://stepik.org/lesson/701989/step/9?unit=702090

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if other not in self.book_list:
            self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
            return self

        if isinstance(other, int):
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)
