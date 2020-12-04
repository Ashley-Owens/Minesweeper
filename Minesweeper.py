# Author: Ashley Owens
# Date: 12/7/2020
# Description: CS 325, Portfolio Project
# Uses PyGame GUI to implement Minesweeper.

try:
    import sys, os, pygame
    from socket import *
    from pygame.locals import *
    from GameBoard import Board
    from BoardTiles import Tiles
    from itertools import cycle
except ImportError:
    print("Could not load module: ImportError.")
    sys.exit(2)


def loadImage(name):
    """
    Loads an image for blitting.
    Args:
        name(string): filename to be loaded
    Raises:
        SystemExit: if image not found
    Returns:
        image: blittable image object
    """
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print('Cannot load image: ', fullname)
        raise SystemExit

    return image


def initializeScreen(x, y):
    """
    Initializes the Pygame surface for blitting game elements.
    Args:
        x (int): screen width
        y (int): screen height
    Returns:
        object: Pygame surface object
    """
    # Initializes the PyGame screen.
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    icon = loadImage('gameicon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Minesweeper')
    return screen


def drawBoard(screen):
    """
    Initializes the game board filled with closed tiles of alternating colors
    while generating a dictionary of rectangle locations for tracking user clicks.
    Args:
        screen (object): Pygame surface
    Returns:
        dict: key = (row, col), value = associated rectangle object
    """
    # Uses itertools to alternate tile colors
    colors = cycle((tile_color1, tile_color2))
    coordinates = {}

    for row in range(rows):
        next(colors)

        # Creates a rectangle object for each position on game board and saves it in a dictionary
        for col in range(cols):
            current = Rect(boxX*row, boxY*col, boxX, boxY)
            coordinates[col, row] = current

            # Draws the tiles to the screen.
            pygame.draw.rect(screen, next(colors), current, 0)

    return coordinates


def makeMove(screen, coordinates, key):
    """
    Given user selected coordinates, opens tiles and calls helper functions to display 
    results of a given move.
    Args:
        screen (object): Pygame surface object
        coordinates (dict): key = (row, col), value = associated rectangle object
        key (tuple): row, col coordinates of user selection
    """
    # Stores the row, col coordinates of the desired move.
    i, j = key

    # Opens the desired tile and adjacent tiles, saving them to a list.
    tiles = board.open_tile(i, j)
    removeTile(screen, coordinates, tiles)

    # Displays Game Over image
    if board.game_lost == True:
        gameOver(screen, loadImage('game-over.png'))

    # Displays Game Won image
    elif board.game_won == True:
        gameOver(screen, loadImage('trophy.png'))
       

def gameOver(screen, image):
    """
    Helper function to display game over messages
    Args:
        screen (object): Pygame surface object
        image (.PNG): image
    """
    image_rect = ((x//2-boxX), (y//2-boxY))
    screen.blit(image, image_rect)


def removeTile(screen, coordinates, tiles):
    """
    Opens tile objects to reveal checkerboard background, tile numbers, and mines.
    Args:
        screen (object): Pygame surface object
        coordinates (dictionary): key = (row, col), value = associated rectangle object
        tiles (list): list of tile objects to be opened on the game board.
    """
    for tile in tiles:
        # Stores the current rect object associated with the tile's coordinates.
        row, col = tile.row, tile.col
        category = tile.category
        current = coordinates[row, col]

        # Alternates opened tiles background color
        if (row + col) % 2 == 0:
            pygame.draw.rect(screen, bg_color1, current, 0)
        else:
            pygame.draw.rect(screen, bg_color2, current, 0)
        
        # Displays mines
        if category == "x":
            image_rect = (8+(boxY*col), 5+(boxX*row))
            screen.blit(loadImage(category +'.png'), image_rect)
        
        # Displays the tile's number
        elif int(category) > 0:
            image_rect = (16+(boxY*col), 17+(boxX*row))
            screen.blit(loadImage(category +'.png'), image_rect)


def placeFlag(screen, key):
    """
    Places a flag in the center of a selected rectangle object. 
    Used for marking suspected mine locations.
    Args:
        screen (object): Pygame surface object
        key (tuple): row, col of flag location
    """
    row, col = key
    flag_img = loadImage("flag.png")
    image_rect = (16+(boxY*col), 15+(boxX*row))
    screen.blit(flag_img, image_rect)


def showBoard(screen, coordinates):
    """
    Enables all tiles to be uncovered and displayed.
    Args:
        screen (object): Pygame surface
        coordinates (dict): key = (row, col), value = associated rectangle object
    """
    colors = cycle((bg_color1, bg_color2))
    mine_img = loadImage("x.png")

    for row in range(rows):
        next(colors)

        for col in range(cols):
            current = coordinates[row, col]
            pygame.draw.rect(screen, next(colors), current, 0)
            category = board.get_board()[row][col].category

            # Places mine images on the board.
            if category == "x":
                image_rect = (8+(boxY*col), 5+(boxX*row))
                screen.blit(mine_img, image_rect)


def blitText(screen, category, rect):
    """
    Helper function for blitting text to the screen.
    Args:
        screen (object): Pygame surface
        category (string): text to display.
        rect (object): rectangle object or location 
    """
    font = pygame.font.SysFont("ariel", 15)
    label = font.render(category, True, tile_color1)
    screen.blit(label, rect)
        

def main():
    """
    Runs game loop.
    """
    while True:
        pygame.display.flip()
        
        # Clicking on window exit button ends game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            # Pressing the space bar enables game cheat.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("The mines are located at: ", board.get_mines())

            # Checks for mouseclicks.
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Left click removes tiles using coordinates dictionary.
                if event.button == 1:
                    for key, value in coordinates.items():
                        if value.collidepoint(event.pos):
                            
                            # Allows user to open tiles when game is lost to view mine locations.
                            if board.game_lost is True:
                                i, j = key
                                removeTile(screen, coordinates, [board.get_board()[i][j]])
                            
                            # Opens tiles to play the game.
                            else:
                                makeMove(screen, coordinates, key)

                # Right click places a flag in suspected mine locations.
                if event.button == 3:
                    for key, value in coordinates.items():
                        if value.collidepoint(event.pos):
                            placeFlag(screen, key)



if __name__ == '__main__':
    # Initializes screen and game board dimensions.
    rows = cols = 8
    mines = 10
    x = y = 480

    # When changing board dimensions, try to keep these variables close to 60
    boxX, boxY = x//rows, y//cols

    # Initializes game board object.
    board = Board(rows, cols, mines)

    # Initializes game board colors.
    bg_color1 = (184, 147, 92)
    bg_color2 = (150, 113, 57)
    tile_color1 = (125, 195, 72) 
    tile_color2 = (166, 227, 120)
    
    # Initializes Pygame surface, blits game board, stores rect objects.
    screen = initializeScreen(x, y)
    coordinates = drawBoard(screen)

    # Runs the game loop.
    main()
