

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

    tile_dict = {
        mine: -2,
        closed: -1,
        zero: 0,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8
    }

    def __init__(self, i, j, tile):
        self.i = i
        self.j = j
        self.tile = str(tile)

    
    @property
    def number(self):
        return self.tile_dict[self.tile]


    @property
    def category(self):
        return self.tile

    def __str__(self):
        return self.tile