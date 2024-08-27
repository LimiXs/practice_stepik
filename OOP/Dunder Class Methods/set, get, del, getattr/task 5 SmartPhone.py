#  https://stepik.org/lesson/701986/step/9?unit=702087
class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        list_apps = [i.name for i in self.apps]
        if app.name not in list_apps:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, contact: dict):
        self.name = "Phone"
        self.phone_list = contact


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
