#  https://stepik.org/lesson/701987/step/12?unit=702088
class InputValues:
    def __init__(self, render):
        # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            input_string = func(*args, **kwargs)
            return [self.__render(arg) for arg in input_string.split()]

        return wrapper

class RenderDigit:
    def __call__(self, value):
        try:
            return int(value)
        except ValueError:
            return None

@InputValues(render=RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)
