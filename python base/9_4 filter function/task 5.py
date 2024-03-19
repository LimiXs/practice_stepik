"""
Подвиг 5. Вводится список email-адресов в одну строчку через пробел.
Среди них нужно оставить только корректно записанные адреса.
Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
А также в адресе должен быть символ "@", а после него символ точки "."
(между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел.
https://stepik.org/lesson/567074/step/7?unit=561348
"""
import string

chars_db = string.ascii_lowercase + string.digits + '_'

mails = input().split()


def is_valid(mail):
    if mail.count('@') != 1 or mail.count('.') < 1:
        return False
    username, domain = mail.split('@')
    if '.' not in domain:
        return False
    domain_name, tld = domain.split('.')
    if not all(char in chars_db for char in username):
        return False
    if not all(char in chars_db for char in domain_name):
        return False
    if not all(char in string.ascii_lowercase for char in tld):
        return False
    return True


valid_mails = filter(is_valid, mails)

print(' '.join(valid_mails))
