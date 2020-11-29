# Minesweeper game board

class Board:

    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.mines = 10
        self.game_state = False

    def new_game(self):
        self.__init__()

    def open_tile(self, i, j):
        if self.game_state or not self.valid_tile(i, j):
            return []

        if self.tiles[i][j] 

    
