"""
https://stepik.org/lesson/701978/step/10?unit=702079
"""
from string import ascii_uppercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase + digits
    PATTERN = r'^\d{4}-\d{4}-\d{4}-\d{4}$'

    @classmethod
    def check_card_number(cls, number: str):
        return bool(re.fullmatch(cls.PATTERN, number))

    @classmethod
    def check_name(cls, name: str):
        if not isinstance(name, str) or len(name.split()) != 2:
            return False
        return all(char in cls.CHARS_FOR_NAME + ' ' for char in name)
