"""
https://stepik.org/lesson/701976/step/10?unit=702077
"""
TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, name):
        self.name = name
