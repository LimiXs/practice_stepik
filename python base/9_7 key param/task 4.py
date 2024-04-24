"""
https://stepik.org/lesson/567077/step/6?unit=561351
"""

lst_in = [
    "Номер;Имя;Оценка;Зачет",
    "1;Портос;5;Да",
    "2;Арамис;3;Да",
    "3;Атос;4;Да",
    "4;д'Артаньян;2;Нет",
    "5;Балакирев;1;Нет"
]

t = tuple(tuple(int(x) if x.isdigit() else x for x in line.split(';')) for line in lst_in)

order = [1, 3, 2, 0]

t_sorted = tuple([tuple(sorted(row, key=lambda x: order.index(row.index(x)))) for row in t])
