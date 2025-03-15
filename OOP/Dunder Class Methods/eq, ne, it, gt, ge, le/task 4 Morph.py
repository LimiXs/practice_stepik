punctuation_chars = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

class Morph:
    def __init__(self, *args):
        self._words = list(map(lambda x: x.strip(punctuation_chars).lower(), args))

    def add_word(self, word: str):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other: str):
        if type(other) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        return other.lower() in self._words


dict_words = [
    Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
    Morph(
        'вектор', 'вектора', 'вектору', 'вектором', 'векторе',
        'векторы', 'векторов', 'векторам','векторами', 'векторах'
    ),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте',
          'эффекты', 'эффектов', 'эффектам','эффектами', 'эффектах'
    ),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
]

text = "Мы будем устанавливать связь завтра днем."
clear_text = map(lambda x: x.strip(punctuation_chars), text.split())

counter = sum(w == morph for w in clear_text for morph in dict_words)
print(counter)
