"""
https://stepik.org/lesson/567079/step/7?unit=561353
"""


def is_free(lst):
    return True if any(map(lambda x: True if '#' in x else False, lst)) else False
