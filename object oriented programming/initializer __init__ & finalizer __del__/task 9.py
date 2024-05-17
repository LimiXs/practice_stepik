class ListObject:
    def __init__(self, data, next_obj=None):
        self.next_obj = next_obj
        self.data = data

    def lin(self, obj):
        self.next_obj = obj
