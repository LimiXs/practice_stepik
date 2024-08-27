class RenderList:
    def __init__(self, type_list='ul'):
        self.type_list = "ol" if type_list == "ol" else "ul"

    def __call__(self, lst):
        return f'<{self.type_list}>\n' + '\n'.join(f'<li>{item}</li>' for item in lst) + '\n' + f'</{self.type_list}>'


'''<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>'''

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)
