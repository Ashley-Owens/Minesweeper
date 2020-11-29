

class Tiles:
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

    board_tiles = [mine, closed, zero, one, two, three, four, five, six, seven, eight]




    def __init__(self, i, j, tile):
        self.i = i
        self.j = j
        self.tile = tile