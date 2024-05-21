"""
https://stepik.org/lesson/567085/step/9?unit=561359
"""
import random
import pprint

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]


# здесь продолжайте программу
def is_valid_position(x, y, P):
    for i in range(max(0, x - 1), min(N, x + 2)):
        for j in range(max(0, y - 1), min(N, y + 2)):
            if P[i][j] == 1:
                return False
    return True


for _ in range(10):
    while True:
        x, y = random.randint(0, N - 1), random.randint(0, N - 1)
        if is_valid_position(x, y, P):
            P[x][y] = 1
            break
