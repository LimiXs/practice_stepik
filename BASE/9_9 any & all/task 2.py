"""
Подвиг 2. Вводится строка вещественных чисел через пробел. Необходимо определить,
есть ли среди них хотя бы одно отрицательное. Вывести True, если это так и False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all.
https://stepik.org/lesson/567079/step/4?unit=561353
"""

data = map(float, input().split())

print(any(map(lambda x: False if x >= 0 else True, data)))