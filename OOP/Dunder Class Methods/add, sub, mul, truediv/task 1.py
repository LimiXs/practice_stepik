# https://stepik.org/lesson/701989/step/6?unit=702090
def is_value_in_list(value, lst):
    return any(isinstance(item, type(value)) and item == value for item in lst)


class NewList:
    def __init__(self, data: list = None):
        self.__data = data

    def __sub__(self, other):
        if type(other) is not NewList:
            sub_list = other
        else:
            sub_list = other.get_list()

        if not sub_list:
            return self

        new_data = []
        for elm in self.__data:
            flag = False
            for sub_elm in sub_list:
                if elm == sub_elm and type(elm) is type(sub_elm):
                    flag = True
                    break
                else:
                    continue
            if not flag:
                new_data.append(elm)

        return NewList(new_data)

    def __rsub__(self, other):
        if type(other) is not NewList:
            first_list = other
        else:
            first_list = other.get_list()

        if not self:
            return first_list

        new_data = []
        for elm in first_list:
            if is_value_in_list(elm, self.__data):
                self.__data.remove(elm)
                continue
            else:
                new_data.append(elm)
        return NewList(new_data)

    def get_list(self):
        return self.__data


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.get_list())
