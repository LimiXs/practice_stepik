"""
Подвиг 5. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra".
То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

Вызовите эту функцию для введенной строки s:
s = input()
Отобразите результат работы функции на экране.

Sample Input:
abrakadabra

Sample Output:
True

https://stepik.org/lesson/567059/step/6?unit=561333
"""
s = input()

check_ra = lambda x: True if "ra" in x else False
print(check_ra(s))