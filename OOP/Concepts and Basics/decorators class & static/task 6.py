"""
https://stepik.org/lesson/701978/step/13?unit=702079
"""


class Message:
    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    messages = {}

    @classmethod
    def add_message(cls, msg: Message):
        cls.messages[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg: Message):
        key = id(msg)
        if key in cls.messages:
            cls.messages.pop(key)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, n):
        if n < 1:
            return ""

        for msg in tuple(cls.messages.values())[-n:]:
            print(msg)

    @classmethod
    def total_messages(cls):
        return len(cls.messages)
