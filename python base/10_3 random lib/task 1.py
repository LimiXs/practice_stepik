"""
Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел. Выполните генерацию вещественной случайной
величины в диапазоне [a; b). Округлите результат до сотых и выведите его на экран.
"""
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

a, b = map(int, input().split())

print(round(random.uniform(a, b), 2))
