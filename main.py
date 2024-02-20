from string import ascii_lowercase

NUMBER = 1_000_000

gen = (y + x for y in ascii_lowercase for x in ascii_lowercase)
for _ in range(0, 50):
    print(next(gen), end=' ')
    