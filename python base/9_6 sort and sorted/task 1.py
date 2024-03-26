"""
https://stepik.org/lesson/567076/step/4?unit=561350
"""
# ввод строки в переменную s (переменную в программе не менять)
s = input()

# здесь продолжайте писать программу
lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(lst)
