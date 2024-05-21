"""
Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си.
На вход программы поступает строка с набором этих нот, записанных через пробел.
Необходимо сформировать список из входной строки с нотами, отсортированными указанным образом.
Результат вывести в виде строки из нот, записанными через пробел.
https://stepik.org/lesson/567077/step/5?unit=561351
"""

notes_db = {
    "до": 1,
    "ре": 2,
    "ми": 3,
    "фа": 4,
    "соль": 5,
    "ля": 6,
    "си": 7,
}

notes = ['до', 'ре', 'до', 'фа', 'соль', 'ре', 'си']

print(*sorted(notes, key=lambda x: notes_db[x]))