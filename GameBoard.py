# Author: Ashley Owens
# Date: 12/7/2020
# Description: CS 325, Portfolio Project
# Minesweeper board class contains primary game logic.

from BoardTiles import Tiles
import random

class Board:
    """
    Contains Minesweeper game logic.
    """
    def __init__(self, rows, cols, mines):
        """
        Initializes minesweeper game and board attributes.
        Args:
            rows (int): number of rows
            cols (int): number of columns
            mines (int): number of mines
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.opened = 0
        self.game_won = False
        self.game_lost = False
        self.board = self.__init__board__()
        self.tiles = self.__init__tiles__()

    def __init__board__(self):
        """
        Initializes game board placing mines in random locations.
        Returns:
            matrix: game board matrix filled with mines
        """
        mines = random.sample(range(0, self.rows * self.cols), self.mines)
        row = (lambda i, j: Tiles.mine if i * self.cols + j in mines else Tiles.zero)
        return [[Tiles(i, j, row(i, j)) for j in range(self.cols)] for i in range(self.rows)]

    def __init__tiles__(self):
        """
        Initializes matrix of game tiles using Tiles class.
        """
        return [[Tiles(i, j, Tiles.closed) for j in range(self.cols)] for i in range(self.rows)]
    
    def __str__(self):
        """
        Useful for debugging and printing game board to the console
        Returns:
            string: game board
        """
        return "\n".join(["  ".join([f"{str(tile):2}" for tile in row]).rstrip() for row in self.tiles])
    
    def get_board(self):
        return self.board

    def new_game(self):
        self.__init__()

    def open_tile(self, i, j):
        """
        Primary game logic for opening a tile. Uses helper methods and performs tile validation, mine 
        redistribution for opening move, tracking opened tiles, and recursively opening adjacent tiles. 
        Args:
            i (int): user selected row
            j (int): user selected column
        Returns:
            list: opened tile objects 
        """
        if self.game_lost or not self.valid_tile(i, j):
            return []

        if self.tiles[i][j].category != Tiles.closed:
            return []

        if self.game_won:
            return []

        # Redistributes mine field and numbers tiles for the first move of the game.
        if self.opened == 0:
            self.adjust_tiles(i, j)
            self.number_tiles()
        
        self.opened += 1
        self.tiles[i][j] = self.board[i][j]

        # Checks for game ending moves.
        if (self.opened + self.mines) == (self.rows * self.cols):
            self.game_won = True
        if self.tiles[i][j].category == Tiles.mine:
            self.game_lost = True

        # Opens adjacent tiles as needed.
        elif self.tiles[i][j].number == 0:
            return self.open_adjacents(i, j, [self.tiles[i][j]])

        return [self.tiles[i][j]]

    def valid_tile(self, i, j):
        """
        Ensures row, col coordinates are valid game board moves.
        Args:
            i (int): user selected row
            j (int): user selected column
        Returns:
            boolean: True if valid else False
        """
        if (i >= 0 and i < self.rows) and (j >= 0 and j < self.cols):
            return True
        return False
    
    def adjust_tiles(self, row, col):
        """
        Helper method used only for the opening move to randomly reallocate mine field.
        Args:
            row (int): user selected row
            col (int): user selected column
        """
        # Iterates through the user selected 3x3 grid.
        for i in [row+1, row-1, row]:
            for j in [col+1, col-1, col]:

                # if the tile is valid and it contains a mine.
                if self.valid_tile(i, j) and self.board[i][j].category == Tiles.mine:
                    random_i = random.randint(0, self.rows - 1)
                    random_j = random.randint(0, self.cols - 1)

                    # Searches for locations to place the mine outside of the 3x3 starting grid.
                    while self.board[random_i][random_j].category == Tiles.mine or (abs(row-random_i) <= 1 and abs(col-random_j) <= 1):
                        random_i = random.randint(0, self.rows - 1)
                        random_j = random.randint(0, self.cols - 1)
                    
                    # Places the mine in a valid random location on the game board.
                    self.board[random_i][random_j] = Tiles(random_i, random_j, Tiles.mine)
                    self.board[i][j] = Tiles(i, j, Tiles.zero)
    
    def number_tiles(self):
        """
        Iterates through game board enumerating tiles according to their proximity to mines.
        """
        # Iterates through entire game board.
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col].category == Tiles.mine:
                    continue
                adjacent_mines = 0

                # Calculates number of mines for each 3x3 grid.
                for i in [row+1, row-1, row]:
                    for j in [col+1, col-1, col]:
                        if (self.valid_tile(i, j) and self.board[i][j].category == Tiles.mine):
                            adjacent_mines += 1
                
                # Sets each game board tile's mine proximity number.
                self.board[row][col] = Tiles(row, col, str(adjacent_mines))

    def open_adjacents(self, row, col, opened_tile):
        """
        Uses recursion to open adjacent tiles.
        Args:
            row (int): user selected row
            col (int): user selected column
            opened_tile (obj): tile object
        Returns:
            list: opened tile objects
        """
        # Doesn't open adjacent mines.
        if self.valid_tile(row, col):
            if self.board[row][col] == Tiles.mine:
                self.tiles[row][col] = self.board[row][col]
                return [Tiles(row, col, Tiles.mine)]
            
            # Iterates through 3x3 grid, only opening closed tiles adjacent to a zero tile.
            for i in [row+1, row-1, row]:
                for j in [col+1, col-1, col]:
                    if (self.valid_tile(i, j) and self.tiles[i][j].category == Tiles.closed):
                        self.opened += 1
                        self.tiles[i][j] = self.board[i][j]
                        opened_tile.append(self.board[i][j])

                        # Checks for a game winning move while opening adjacent tiles.
                        if (self.opened + self.mines) == (self.rows * self.cols):
                            self.game_won = True

                        # If an adjacent tile is zero, recursively opens that tile's adjacent tiles.
                        if self.board[i][j].category == Tiles.zero:
                            self.open_adjacents(i, j, opened_tile)
        return opened_tile

    def get_mines(self):
        """
        Helper method for obtaining current minefield.
        Returns:
            list: all mine coordinates in an (i, j) tuple
        """
        mines = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].category == Tiles.mine:
                    mines.append((i, j))
        return mines




# game = Board(8, 8, 10)
# print(game.tiles[0][0].category)
# print('Opening move')
# print(game)
# game.open_tile(2, 2)
# print(game)
# print("second move")
# game.open_tile(2, 3)
# print(game)


    



    
