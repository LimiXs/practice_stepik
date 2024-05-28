#  https://stepik.org/lesson/701983/step/5?unit=702084
class Clock:
    def __init__(self):
        self.__time = 0

    @staticmethod
    def __check_time(tm: int):
        return isinstance(tm, int) and 0 <= tm < 100000

    def get_time(self):
        return self.__time

    def set_time(self, tm: int):
        if self.__check_time(tm):
            self.__time = tm


clock = Clock()
clock.set_time(4530)
