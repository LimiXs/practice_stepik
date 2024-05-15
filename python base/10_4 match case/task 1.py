"""
https://stepik.org/lesson/988826/step/7?unit=996311
"""
cmd = input()

match cmd.lower():
    case 'top':
        print('Команда top')
    case 'bottom':
        print('Команда bottom')
    case 'right':
        print('Команда right')
    case 'left':
        print('Команда left')
    case _:
        print('Неверная команда')
