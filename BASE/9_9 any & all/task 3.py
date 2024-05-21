"""
https://stepik.org/lesson/567079/step/5?unit=561353
"""


def is_string(lst):
    return all(isinstance(item, str) for item in lst)
