"""
https://stepik.org/lesson/567078/step/6?unit=561352
"""


def get_even_sum(it):
    result = 0
    for v in it:
        if isinstance(v, bool):
            continue
        if isinstance(v, int) and v % 2 == 0:
            result += v

    return result
