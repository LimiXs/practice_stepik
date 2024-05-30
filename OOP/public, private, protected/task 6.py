class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__link_list = []

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

        self.__link_list.append(obj)

    def remove_obj(self):
        self.__link_list.pop(len(self.__link_list) - 1)
        if len(self.__link_list) == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.__link_list[len(self.__link_list) - 1]
            self.tail.set_next(None)

    def get_data(self):
        result = []
        for obj in self.__link_list:
            result.append(obj.get_data())
        return result


ob = ObjList("данные 1")
