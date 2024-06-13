#  https://stepik.org/lesson/701986/step/7?unit=702087
class Course:
    pass


class Module:
    pass


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == "title":
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == "practices" or key == "duration":
            if not isinstance(value, int) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

course = Course("Python ООП")

module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)

module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)