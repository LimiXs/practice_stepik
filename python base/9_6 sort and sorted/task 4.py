"""
https://stepik.org/lesson/567076/step/7?unit=561350
"""
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

result = [a + b for a, b in zip(list1, list2)]

print(' '.join(map(str, result)))
