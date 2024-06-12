#  https://stepik.org/lesson/701985/step/13?unit=702086

class TVProgram:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @name.setter
    def name(self, value):
        self.__name = value

    @uid.setter
    def uid(self, value):
        self.__id = value


pr = TVProgram("Первый канал")

pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
