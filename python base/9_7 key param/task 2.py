"""
https://stepik.org/lesson/567077/step/4?unit=561351
"""

lst_in = [
    'ножницы=100',
    'котелок=500',
    'спички=20',
    'зажигалка=40',
    'зеркальце=50'
]

dict_data = {}

for item in lst_in:
    split_item = item.split('=')
    dict_data[split_item[0]] = int(split_item[1])

print(*sorted(dict_data, reverse=True, key=lambda x: dict_data[x]))
