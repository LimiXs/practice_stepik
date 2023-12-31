"""
Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.

Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел,
записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
Результат вывести на экран командой (lst - ссылка на коллекцию): print(lst).

Sample Input:
list
-5 6 8 11 0 111 -456 3

Sample Output:
[-5, 6, 8, 11, 0, 111, -456, 3]

https://stepik.org/lesson/567061/step/6?unit=561335
"""


def one_f(tp='list'):
    def two_f(data):
        return data if tp == 'list' else tuple(data)

    return two_f


type_input = input()
input_data = list(map(int, input().split()))

f = one_f(type_input)
lst = f(input_data)
print(lst)
