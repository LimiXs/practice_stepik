"""
https://stepik.org/lesson/567073/step/3?unit=561347
"""
s = input().split()
s = list(map(float, s))

print(*[s[x] for x in range(0, 3) if x in (0, 1, 2)])
