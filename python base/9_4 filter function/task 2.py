"""
https://stepik.org/lesson/567074/step/4?unit=561348
"""

lst_in = ['зонт=1000',
          'палатка=10000',
          'спички=22',
          'котелок=543']


def check_sum(trade):
    price = int(trade[1])
    return True if price >= 500 else False


things = tuple(map(tuple, (item.split('=') for item in lst_in)))

print(*[x[0] for x in filter(check_sum, things)])
