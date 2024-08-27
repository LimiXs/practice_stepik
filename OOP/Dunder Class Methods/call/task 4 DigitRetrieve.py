class DigitRetrieve:
    def __call__(self, value, *args, **kwargs):
        try:
            return int(value)
        except ValueError:
            return None
