"""
Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел.
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и
отобразите результат на экран в виде последовательности чисел, записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.

P.S. Теория сортировки в видео предыдущего шага.

Sample Input:
8 11 -6 3 0 1 1

Sample Output:
-6 0 1 1 3 8 11
https://stepik.org/lesson/567058/step/10?unit=561332
"""


def divide_list(arr):
    if len(arr) <= 1:
        return [arr] if arr else []

    middle = len(arr) // 2
    left = divide_list(arr[:middle])
    right = divide_list(arr[middle:])

    return merge(left, right)


def merge(left, right):
    merged = []

    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


data = list(map(int, input().split()))
sorted_list = divide_list(data)

result_str = ' '.join(map(str, sorted_list))
print(result_str.replace("[", "").replace("]", ""))
