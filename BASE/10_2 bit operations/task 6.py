"""
https://stepik.org/lesson/567084/step/9?unit=561358
"""
data = input()
KEY = 123

print(''.join(list(map(lambda x: chr(ord(x) ^ KEY), data))))
