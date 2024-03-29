"""
Подвиг 3. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
используя следующий словарь для замены русских букв на соответствующее латинское написание:
Функция должна возвращать преобразованную строку. Замены делать без учета регистра
(исходную строку перевести в нижний регистр - малые буквы).
Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и,
кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису.
Полученный результат должен возвращаться в виде строки.
Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
s = input()
Результат отобразите на экране.

Sample Input:
Декораторы - это круто!

Sample Output:
dekoratory-eto-kruto-
https://stepik.org/lesson/567063/step/4?unit=561337
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replace_chars(chars=" !?"):
    def decorator(func):
        def wrapper(s):
            result = func(s)
            for char in chars:
                result = result.replace(char, '-')
            while '--' in result:
                result = result.replace('--', '-')
            return result
        return wrapper
    return decorator


@replace_chars(chars="?!:;,. ")
def cyrillic_to_latin(s):
    return ''.join(t.get(c, c) for c in s.lower())


s = input()
print(cyrillic_to_latin(s))
