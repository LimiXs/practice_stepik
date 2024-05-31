import random


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N: int, M: int):
        self._n = N
        self._m = M
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
        self.init()

    def init(self):
        coordinates = []
        while len(coordinates) < self._m:
            i, j = self.get_random_coords(self._n), self.get_random_coords(self._n)

            if (i, j) not in coordinates:
                coordinates.append((i, j))

        for i, j in coordinates:
            self.pole[i][j].mine = True

        ind = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in ind if 0 <= x+i < self._n and 0 <= y+j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(' '.join([f"{self.get_cell_value(cell)}" for cell in row]))

    @staticmethod
    def get_cell_value(cell: Cell) -> str:
        if not cell.fl_open:
            return '#'
        else:
            if cell.mine:
                return '*'
            else:
                return str(cell.around_mines)

    @staticmethod
    def get_random_coords(n):
        return random.randint(0, n - 1)


pole_game = GamePole(10, 12)
