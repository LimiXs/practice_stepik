# https://stepik.org/lesson/701990/step/9?unit=702091
filenames = [
    "boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
    "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"
]


class FileAcceptor:
    def __init__(self, *extensions: str):
        self.extensions = list(extensions)

    def __call__(self, file: str) -> bool:
        return file.split('.')[-1] in self.extensions

    def __add__(self, other: 'FileAcceptor') -> 'FileAcceptor':
        combined_extensions = self.extensions + other.extensions
        return FileAcceptor(*combined_extensions)


acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)
