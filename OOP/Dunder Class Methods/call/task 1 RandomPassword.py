#  https://stepik.org/lesson/701987/step/4?unit=702088
from random import randint, choice


class RandomPassword:
    def __init__(self,psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        password = "".join(
            choice(self.__psw_chars) for _ in range(randint(self.__min_length, self.__max_length))
        )

        return password


min_length = 5
max_length = 10
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

lst_pass = [RandomPassword(psw_chars, min_length, max_length)() for _ in range(3)]
print(lst_pass)

rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()
print(psw)
