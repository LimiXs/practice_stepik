#  https://stepik.org/lesson/701984/step/6?unit=702085
class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 2 <= len(model) <= 100:
            self.__model = model
        