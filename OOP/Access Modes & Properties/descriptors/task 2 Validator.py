#  https://stepik.org/lesson/701985/step/10?unit=702086
class StringValue:
    def __init__(self, validator=None):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator is None or self.validator.validate(value):
            setattr(instance, self.name, value)


class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return self.min_length <= len(string) <= self.max_length and isinstance(string, str)


class RegisterForm:
    login = StringValue(validator=ValidateString(min_length=3, max_length=100))
    password = StringValue(validator=ValidateString(min_length=3, max_length=100))
    email = StringValue(validator=ValidateString(min_length=3, max_length=100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        return f"""
            <form>
            Логин: {self.login}
            Пароль: {self.password}
            Email: {self.email}
            </form>
        """
