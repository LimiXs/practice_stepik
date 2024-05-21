"""
https://stepik.org/lesson/567085/step/8?unit=561359
"""
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

my_list = input().split()
sampled_list = random.sample(my_list, 3)

print(*sampled_list)
