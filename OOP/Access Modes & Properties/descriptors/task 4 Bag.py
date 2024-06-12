#  https://stepik.org/lesson/701985/step/12?unit=702086
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if sum(thing.weight for thing in self.things) + thing.weight <= self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx):
        self.things.pop(indx)

    def get_total_weight(self):
        return sum(thing.weight for thing in self.things)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        