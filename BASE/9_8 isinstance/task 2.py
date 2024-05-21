"""
https://stepik.org/lesson/567078/step/5?unit=561352
"""


def get_sum(it):
    result = 0

    for v in it:
        if isinstance(v, bool):
            continue

        if isinstance(v, int):
            result += v
    return result
