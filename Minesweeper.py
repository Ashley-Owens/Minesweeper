# Author: Ashley Owens
# Date: 12/7/2020
# Description: CS 325, Portfolio Project
# Uses PyGame to implement Minesweeper.

try:
    import sys, os, pygame
    from socket import *
    from pygame.locals import *
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



def main():
    """
    Initializes game board screen and runs game loop.
    """
    pygame.init()
    x, y = 700, 740

    # Initializes the PyGame screen, background, and mapping dict.
    screen = pygame.display.set_mode((x, y))
    icon = loadImage('gameicon.png')
    # background = loadImage('board_bg.jpg')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Minesweeper')
    # coordinates = update_board(screen, background)
    pygame.display.update()
    clicks = []

    # Initiates the game loop.
    while True:

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

main()