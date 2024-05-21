"""
https://stepik.org/lesson/567076/step/8?auth=login&unit=561350
"""

lst_in = [
    'смартфон:120000',
    'яблоко:2',
    'сумка:560',
    'брюки:2500',
    'линейка:10',
    'бумага:500'
]

dct = {}

for elm in lst_in:
    split_elm = elm.split(':')
    dct[int(split_elm[1])] = split_elm[0]


def get_three_min(data: dict) -> list:
    sorted_items = sorted(data.items())
    return [value for key, value in sorted_items[:3]]


print(*get_three_min(dct))
