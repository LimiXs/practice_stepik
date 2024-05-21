"""
https://stepik.org/lesson/701975/step/8?unit=702076
"""
WARNING_MSG = "Отображение данных закрыто"


# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data: list):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data: list):
        self.data = data

    def show_table(self):
        print(' '.join(self.data) if self.is_show else WARNING_MSG)

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
        else:
            print(WARNING_MSG)

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
        else:
            print(WARNING_MSG)

    def set_show(self, fl_show: bool):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
