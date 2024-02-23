def my_numbers(n):
    a, b, c = 1, 1, 1
    for i in range(n):
        if i in (0, 1):
            yield 1
        elif i == 2:
            yield 1
            a, b, c = b, c, a + b + c
        else:
            yield c
            a, b, c = b, c, a + b + c


gen = my_numbers(int(input()))

for y in gen:
    print(y, end=' ')
