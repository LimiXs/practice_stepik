"""
https://stepik.org/lesson/567078/step/4?unit=561352
"""


def get_add(a, b):
    if isinstance(a, (int, float, bool)) and isinstance(b, (str, bool)) or \
       isinstance(b, (int, float, bool)) and isinstance(a, (str, bool)):
        return None
    else:
        return a + b
    