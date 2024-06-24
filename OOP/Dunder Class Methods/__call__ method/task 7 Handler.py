class Handler:
    def __init__(self, method='GET'):
        self.method = method

    def __call__(self, func):
        pass



@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"