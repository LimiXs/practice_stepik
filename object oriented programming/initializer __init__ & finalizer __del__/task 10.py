class Cell:
    def __init__(self, around_mines, mine, fl_open=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False


class GamePole:
    pass


c1 = Cell(4, True)
