#  https://stepik.org/lesson/701987/step/5?unit=702088
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename: str, *args, **kwargs):
        parts = filename.rsplit('.', 1)
        if len(parts) > 1 and parts[1] in self.extensions:
            return True
        return False


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
