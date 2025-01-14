# https://stepik.org/lesson/701988/step/6?unit=702089
class WordString:
    def __init__(self, *args):
        self.string = ""


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")