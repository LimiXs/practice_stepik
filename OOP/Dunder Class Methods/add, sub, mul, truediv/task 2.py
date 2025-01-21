class ListMath:
    def __init__(self, data: list = None):
        self.__data = [x for x in data if type(x) in (int, float)]
        self.lst_math = None