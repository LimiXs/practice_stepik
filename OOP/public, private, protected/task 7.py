#  https://stepik.org/lesson/701983/step/12?unit=702084
import random
from string import ascii_lowercase, ascii_uppercase, digits


class EmailValidator:
    CHARS = ascii_lowercase+ ascii_uppercase + digits + '._@'
    EMAIL_RANDOM_CHARS = ascii_lowercase+ ascii_uppercase + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.CHARS):
            return False

        email_parts = email.split('@')
        if len(email_parts) != 2:
            return False

        if len(email_parts[0]) > 100 or len(email_parts[1]) > 50:
            return False

        if '.' not in email_parts[1]:
            return False

        if email.count('..') > 0:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        n = random.randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return ''.join(cls.EMAIL_RANDOM_CHARS[random.randint(0, length)] for _ in range(n)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email: str):
        return isinstance(email, str)
