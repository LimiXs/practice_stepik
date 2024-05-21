"""
Необходимо определить функцию-генератор,
которая бы выдавала пароль длиной N символов из случайных букв,
цифр и некоторых других знаков.
https://stepik.org/lesson/567072/step/5?unit=561346
"""
import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def generate_passwrod(N):
    while True:
        yield "".join([chars[random.randint(1, len(chars)) - 1] for _ in range(N)])


gen_pas = generate_passwrod(int(input()))

for _ in range(0, 5):
    print(next(gen_pas))
