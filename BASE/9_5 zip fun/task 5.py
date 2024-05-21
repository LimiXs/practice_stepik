"""
https://stepik.org/lesson/567075/step/7?unit=561349
"""
# считывание строки в переменную s (эту переменную в программе не менять)
s = input()
s = s.split()

gen_zip = zip(s, [i for i in range(0, len(s))])
lst = list(gen_zip)
