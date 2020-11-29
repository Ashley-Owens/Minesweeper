# Minesweeper game board

from tiles import Tiles
import random

class Board:

    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.mines = 10
        self.opened = 0
        self.game_state = False
        self.board = self.__init__board__()
        self.tiles = self.__init__tiles__()

    def __init__board__(self):
        mines = random.sample(range(0, self.rows * self.cols), self.mines)
        row = (
            lambda i, j: Tiles.mine
            if i * self.cols + j in mines
            else Tiles.zero
        )
        return [[Tiles(i, j, row(i, j)) for j in range(self.cols)] for i in range(self.rows)]

    def __init__tiles__(self):
        return [[Tiles(i, j, Tiles.closed) for j in range(self.cols)]
            for i in range(self.rows)]
    

    def new_game(self):
        self.__init__()

    def open_tile(self, i, j):
        if self.game_state or not self.valid_tile(i, j):
            return []

        if self.tiles[i][j].category != Tiles.closed:
            return []

        if self.opened == 0:
            self.adjust_tiles(i, j)
            self.number_tiles()


    def valid_tile(self, i, j):
        if (i >= 0 and i < self.rows) and (j >= 0 and j < self.cols):
            return True
        return False

    
    def adjust_tiles(self, row, col):
        for i in [row+1, row-1, row]:
            for j in [col+1, col-1, col]:

                # if the starting tile is valid and it contains a mine.
                if self.valid_tile(i, j) and self.board[i][j].category == Tiles.mine:
                    random_i = random.randint(0, self.rows - 1)
                    random_j = random.randint(0, self.cols - 1)

                    # Search for a valid location on the game board to place the mine.
                    while self.board[random_i][random_j].category == Tiles.mine or (abs(row-random_i) <= 1 and abs(col-random_j) <= 1):
                        random_i = random.randint(0, self.rows - 1)
                        random_j = random.randint(0, self.cols - 1)
                    
                    # Places the mine in a valid random location on the game board.
                    self.board[random_i][random_j] = Tiles(random_i, random_j, Tiles.mine)
                    self.board[i][j] = Tiles(i, j, Tiles.zero)
                        





    



    
