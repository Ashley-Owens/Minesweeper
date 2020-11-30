# Author: Ashley Owens
# Date: 12/7/2020
# Description: CS 325, Portfolio Project
# Uses PyGame to implement Minesweeper.

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
    :param name: filename to be loaded (string)
    :return: image object, rectangular area of the image object
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
    # Initializes the PyGame screen and background.
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    icon = loadImage('gameicon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Minesweeper')
    drawBoard(screen)


def drawBoard(screen):

    colors = cycle((bg_color1, bg_color2))
    mine_img = loadImage("mine.png")
    zero_img = loadImage("zero.png")
    rect_list = []

    for row in range(rows):
        next(colors)

        for col in range(cols):
            current = Rect(60*row, 60*col, boxX, boxY)
            rect_list.append(current)
            pygame.draw.rect(screen, next(colors), current, 0)
            category = board.get_board()[row][col].category

            # Places mine images on the board.
            if category == "x":
                image_rect = (8+(60*row), 5+(60*col))
                screen.blit(mine_img, image_rect)
            
            # Places zeroes on the board.
            # else:
            #     image_rect = (15+(60*row), 13+(60*col))
            #     screen.blit(zero_img, image_rect)
    
    print(rect_list)



def main():
    """
    Initializes game board screen and runs game loop.
    """
    initializeScreen(x, y)
    clicks = []

    # Initiates the game loop.
    while True:
        
        pygame.display.flip()

        # Clicking on window exit button ends game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # # Locates click coordinates in dict and adds red outline to enhance footprint.
            # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #     for click in range(0, 1):
            #         for key, value in coordinates.items():
            #             if value.collidepoint(event.pos):
            #                 clicks.append(key)
            #                 rect = pygame.Rect(value)
            #                 inflated = rect.inflate(60, 60)
            #                 pygame.draw.rect(background, red, inflated, 4)
            #                 screen.blit(background, (0, 0))
            #                 update_board(screen, background)
            #                 pygame.display.update()
            #     print(clicks)


if __name__ == '__main__':
    board = Board()
    rows, cols = 8, 8
    x, y = 480, 480
    boxX = x/8
    boxY = y/8
    bg_color1 = (184, 147, 92)
    bg_color2 = (150, 113, 57)
    tile_color1 = (144, 207, 63)
    tile_color2 = (176, 233, 102)
    # myFont = pygame.font.SysFont("ariel", 15)
    # label = myFont.render(str(category), 20, (0, 0, 0))
    # screen.blit(label, current)

    main()