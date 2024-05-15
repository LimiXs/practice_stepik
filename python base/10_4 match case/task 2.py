"""
https://stepik.org/lesson/988826/step/9?unit=996311
"""


def get_data(value):
    match value:
        case int() as data if data > 0:
            return data
        case float() as data if -100 <= data <= 100:
            return data
        case str():
            return value
    return None
