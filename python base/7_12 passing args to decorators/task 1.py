"""
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию,
которая преобразовывает эту строку в список чисел и возвращает их сумму.
Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.

Sample Input:
5 6 3 6 -4 6 -1

Sample Output:
26
"""


def start_from(start=0):
    def decorator(func):
        def wrapper(x):
            result = start + func(x)
            return result
        return wrapper
    return decorator


@start_from(start=5)
def get_sum(data):
    return sum(list(map(int, data.split())))


input_data = input()
print(get_sum(input_data))
