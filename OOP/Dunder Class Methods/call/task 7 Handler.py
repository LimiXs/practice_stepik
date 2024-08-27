# https://stepik.org/lesson/701987/step/10?unit=702088
class Handler:
    def __init__(self, methods=('GET', )):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request):
            raw_method = request.get('method', 'GET')
            if raw_method in self.__methods:
                method = raw_method.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

print(contact({'method': 'POST'}))

