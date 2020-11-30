# Minesweeper game board with primary game logic

from BoardTiles import Tiles
import random

class Board:

    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.mines = 10
        self.opened = 0
        self.game_won = False
        self.game_lost = False
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
    
    def get_board(self):
        return self.board

    def new_game(self):
        self.__init__()

    def open_tile(self, i, j):
        if self.game_lost or not self.valid_tile(i, j):
            return []

        if self.tiles[i][j].category != Tiles.closed:
            return []

        if self.opened == 0:
            self.adjust_tiles(i, j)
            self.number_tiles()
        
        self.opened += 1
        self.tiles[i][j] = self.board[i][j]

        if self.opened + self.mines == (self.rows * self.cols):
            self.game_won = True

        if self.tiles[i][j].category == Tiles.mine:
            self.game_lost = True

        elif self.tiles[i][j].number >= 0:
            if self.tiles[i][j].number == 0:
                return self.open_adjacents(i, j, [self.tiles[i][j]])

        return [self.tiles[i][j]]


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
    
    def number_tiles(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col].category == Tiles.mine:
                    continue
                adjacent_mines = 0

                for i in [row+1, row-1, row]:
                    for j in [col+1, col-1, col]:
                        if (self.valid_tile(i, j) and self.board[i][j].category == Tiles.mine):
                            adjacent_mines += 1
                
                self.board[row][col] = Tiles(i, j, str(adjacent_mines))

    def open_adjacents(self, row, col, opened_tile):
        if self.valid_tile(row, col):
            if self.board[row][col] == Tiles.mine:
                self.tiles[row][col] = self.board[row][col]
                return [Tiles(row, col, Tiles.mine)]
            
            for i in [row+1, row-1, row]:
                for j in [col+1, col-1, col]:
                    if (self.valid_tile(i, j) and self.tiles[i][j].category == Tiles.closed):
                        self.opened += 1
                        self.tiles[i][j] = self.board[i][j]
                        opened_tile.append(self.board[i][j])

                        if (self.opened + self.mines) == (self.rows * self.cols):
                            self.game_won = True

                        if self.board[i][j].category == Tiles.zero:
                            self.open_adjacents(i, j, opened_tile)
        return opened_tile



    def __str__(self):
        return "\n".join(
            [
                "  ".join([f"{str(tile):2}" for tile in row]).rstrip()
                for row in self.tiles
            ]
        )

# game = Board()
# print('Opening move')
# game.open_tile(2, 2)
# print(game)
# print("second move")
# game.open_tile(2, 3)
# print(game)


    



    
