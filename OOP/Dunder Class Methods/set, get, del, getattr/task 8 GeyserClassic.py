#  https://stepik.org/lesson/701986/step/12?unit=702087
import time
from typing import Union

DATE_ATTR = "date"


class Mechanical:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            pass
        else:
            super().__setattr__(key, value)


class Aragon:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        super().__setattr__(key, value)


class Calcium:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        super().__setattr__(key, value)


class GeyserClassic:
    MIN_DATE_FILTER = 0
    MAX_DATE_FILTER = 100  # максимальное время работы фильтра(любого)
    SLOTS_GUIDE = {
        1: Mechanical,
        2: Aragon,
        3: Calcium
    }

    def __init__(self):
        self.slots = {
            1: None,
            2: None,
            3: None
        }

    def add_filter(self, slot_num, filter: Union[Mechanical, Aragon, Calcium]):
        if slot_num in self.slots and isinstance(filter, GeyserClassic.SLOTS_GUIDE[slot_num]):
            if self.slots[slot_num] is None:
                self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if slot_num in self.slots and self.slots[slot_num] is not None:
            self.slots[slot_num] = None

    def get_filters(self):
        return tuple([x for x in self.slots.values()])

    def water_on(self):
        first_condition = all(x is not None for x in self.slots.values())
        if not first_condition:
            return False
        second_condition = all(
            self.MIN_DATE_FILTER <= time.time() - filter.date <= self.MAX_DATE_FILTER
            for filter in self.slots.values()
        )
        return second_condition


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
