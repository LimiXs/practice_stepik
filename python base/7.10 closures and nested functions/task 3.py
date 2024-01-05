"""
Подвиг 3. Используя замыкания функций, объявите внутреннюю функцию,
которая заключает в тег h1 строку s (s - строка, параметр внутренней функции).
Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания.
Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>

Sample Input:
Balakirev

Sample Output:
<h1>Balakirev</h1>
https://stepik.org/lesson/567061/step/4?unit=561335
"""


def teg(text):
    def decor():
        return f'<h1>{text}</h1>'

    return decor


fun = teg(input())
print(fun())
