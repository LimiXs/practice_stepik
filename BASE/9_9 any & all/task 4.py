"""
Подвиг 4. Вводятся оценки студента в одну строчку через пробел. Необходимо определить,
имеется ли в этом списке хотя бы одна оценка ниже тройки. Если это так,
то вывести на экран строку "отчислен", иначе - "учится".

Задачу реализовать с использованием одной из функций: any или all.
https://stepik.org/lesson/567079/step/6?unit=561353
"""

data = map(int, input().split())

print("учится" if all(map(lambda x: x > 2, data)) else "отчислен")