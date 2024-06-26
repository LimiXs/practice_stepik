"""
https://stepik.org/lesson/567077/step/7?unit=561351
"""

lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан", 'Арамис=лейтенант', 'Балакирев=рядовой']

ranks = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']

# Входные данные (пример)
data = lst_in

# Преобразование входных данных в список
lst = [line.split('=') for line in data]

# Сортировка списка по возрастанию званий
lst.sort(key=lambda x: ranks.index(x[1]))
