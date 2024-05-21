"""
https://stepik.org/lesson/567072/step/6?unit=561346
"""
import random
from string import ascii_lowercase, ascii_uppercase


def generate_email(N):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        email = ''.join(random.choice(chars) for _ in range(N)) + '@mail.ru'
        yield email


random.seed(1)
gen = generate_email(int(input()))
for _ in range(5):
    print(next(gen))
