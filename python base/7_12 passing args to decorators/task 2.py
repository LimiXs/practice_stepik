"""
Подвиг 2. Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
Определите декоратор для этой функции, который имеет один параметр tag,
определяющий строку с названием тега и начальным значением "h1".
Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
Пример заключения строки "python" в тег h1: <h1>python</h1>
Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.
https://stepik.org/lesson/567063/step/3?unit=561337
"""


def decorate_text(tag="h1"):
    def decorator(func):
        def wrapper(text):
            result = func(text)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator


@decorate_text(tag="div")
def make_lower(text):
    return text.lower()


s = input()
print(make_lower(s))
