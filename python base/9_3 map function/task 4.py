"""
Подвиг 4. На вход программы поступает строка в формате:

ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

Необходимо с помощью функции map преобразовать ее в кортеж tp вида:

tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
https://stepik.org/lesson/567073/step/6?unit=561347
"""

# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

tp = []

for elm in s_lst:
    tp.append(elm.split('='))

tp = tuple(map(tuple, tp))
