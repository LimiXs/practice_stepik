# https://stepik.org/lesson/701989/step/12?unit=702090

# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step
#         self.size = size
#
#     def __call__(self, *args, **kwargs):
#         result = []
#         size_matrix = len(args[0])
#
#         for elm in args:
#             if any(not isinstance(x, (int, float)) for x in elm) or len(elm) != size_matrix:
#                 raise ValueError("Неверный формат для первого параметра matrix.")
#
#         for i in range(0, size_matrix, self.step[0]):
#
#         return result
