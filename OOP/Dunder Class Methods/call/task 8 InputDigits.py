#  https://stepik.org/lesson/701987/step/11?unit=702088
class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.func().split()))


input_dg = InputDigits(input)
res = input_dg()
