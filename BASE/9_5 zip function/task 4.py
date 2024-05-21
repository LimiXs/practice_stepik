"""
Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную таблицу из
трех столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы из
слов, записанных через пробел (в каждой строчке).
https://stepik.org/lesson/567075/step/6?unit=561349
"""
from builtins import input


def create_table(input_data):
    words = input_data.split()
    words = words[:len(words) - len(words) % 3]
    for row in zip(words[::3], words[1::3], words[2::3]):
        print(' '.join(row))


input_string = input()
create_table(input_string)
