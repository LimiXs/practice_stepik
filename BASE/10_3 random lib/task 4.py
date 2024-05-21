"""
Подвиг 5. Вводится таблица целых чисел, записанных через пробел. Необходимо перемешать столбцы этой таблицы,
используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
"""
import sys
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']
lst_in = [list(map(int, line.split())) for line in lst_in]

transposed = list(map(list, zip(*lst_in)))

random.shuffle(transposed)

shuffled = list(map(list, zip(*transposed)))

for row in shuffled:
    print(' '.join(map(str, row)))
