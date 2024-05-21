"""
https://stepik.org/lesson/567078/step/7?unit=561352
"""


def get_list_dig(lst):
    result = []
    for v in lst:
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)):
            result.append(v)

    return result
