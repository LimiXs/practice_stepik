# https://stepik.org/lesson/701990/step/10?unit=702091
class BaseMoney:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    def set_cb(self, cb):
        self.__cb = cb

    def get_cb(self):
        return self.__cb

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

class MoneyR(BaseMoney):
    def __init__(self, volume=0):
        super().__init__(volume)

class MoneyD(BaseMoney):
    def __init__(self, volume=0):
        super().__init__(volume)

class MoneyE(BaseMoney):
    def __init__(self, volume=0):
        super().__init__(volume)