"""
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
https://stepik.org/lesson/567072/step/7?unit=561346
"""


def generate_primes():
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


gen = generate_primes()

for _ in range(0, 20):
    print(next(gen), end=' ')
