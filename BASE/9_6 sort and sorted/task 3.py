"""
Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
Необходимо выбрать из них четыре наибольших уникальных значения.
Результат вывести на экран в порядке их убывания в одну строчку через пробел.
"""
data = set(map(int, input().split()))
data = sorted(list(data), reverse=True)
for i in range(0, 4):
    print(data[i], end=' ')