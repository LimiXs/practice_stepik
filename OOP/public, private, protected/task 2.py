#  https://stepik.org/lesson/701983/step/6?unit=702084
class Money:
    def __init__(self, money=0):
        self.__money = money

    def get_money(self):
        return self.__money

    def set_money(self, money: int):
        if self.__check_money(money):
            self.__money = money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money: int):
        return isinstance(money, int) and money >= 0
