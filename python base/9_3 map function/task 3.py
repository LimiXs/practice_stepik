"""
Подвиг 3. Вводится таблица целых чисел. Используя функцию map и генератор списков,
преобразуйте список строк lst_in (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.
Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
https://stepik.org/lesson/567073/step/5?unit=561347
"""
import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    '8 11 -5',
    '3 4 10',
    '-1 -2 3',
    '-4 5 6'
]

lst2D = []
for elm in lst_in:
    lst2D.append(list(map(int, elm.split())))

print(lst2D)
