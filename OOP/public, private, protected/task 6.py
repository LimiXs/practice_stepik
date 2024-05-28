#  https://stepik.org/lesson/701983/step/11?unit=702084
class ObjList:
    def __init__(self):
        self.__list = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        self.__list.append(obj)
        self.head = self.__list[0]
        self.tail = self.__list[-1]

    def remove_obj(self):
        if len(self.__list) > 0:
            self.__list.pop(len(self.__list) - 1)

            self.tail = self.__list[-1]

    def get_data(self):
        return self.__list