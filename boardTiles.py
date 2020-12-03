# Author: Ashley Owens
# Date: 12/7/2020
# Description: CS 325, Portfolio Project
# Minesweeper Tile class for tracking tile numbers, unopened tiles, and mines.

class Tiles:
    """
    Tracks tile attributes for Minesweeper game board.
    """
    # Global variables
    mine = "x"
    closed = "c"
    zero = "0"
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"

    def __init__(self, i, j, tile):
        """Initializes tile attributes for tracking location and type.
        Args:
            i (int): tile row position
            j (int): tile column position
            tile (string): tile category (one of the global variables)
        """
        self.i = i
        self.j = j
        self.tile = str(tile)
    
    def __str__(self):
        """
        Useful for debugging and printing the tile type to the console.
        Returns:
            string: tile category (one of the global variables)
        """
        return self.tile
    
    @property
    def row(self):
        return self.i

    @property
    def col(self):
        return self.j

    @property
    def category(self):
        return self.tile

    