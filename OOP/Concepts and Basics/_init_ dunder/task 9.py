"""
https://stepik.org/lesson/701975/step/11?unit=702076
"""


class ListObject:
    def __init__(self, data, next_obj=None):
        self.next_obj = next_obj
        self.data = data

    def lin(self, obj):
        self.next_obj = obj


lst_in = ['1', '3', '3', '2',]

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.lin(obj_new)
    obj = obj_new
