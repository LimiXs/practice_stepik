"""
Подвиг 1. Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными.
Вывести True, если это так и False - в противном случае.
Задачу реализовать с использованием одной из функций: any или all.
https://stepik.org/lesson/567079/step/3?unit=561353
"""


def are_all_numbers_even(numbers_string):
    numbers = map(int, numbers_string.split())
    return all(number % 2 == 0 for number in numbers)


numbers_string = input()
print(are_all_numbers_even(numbers_string))
