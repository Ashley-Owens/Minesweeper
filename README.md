# Minesweeper

## Objective
Clear a rectangular board containing hidden mines without detonating any of them. Cleared tiles display a number, which depicts the number of neighboring mines in the tiles surrounding it.    

![Minesweeper](images/Minesweeper.gif)


## Game Rules
1. The first click is a freebie, you can never click a mine during an opening move.
2. Only closed/covered tiles are available for clicking. If you uncover a tile containing a mine, the game is over. However, I have enabled clicking after the game is lost so you can view mine locations.
3. Uncovered blank tiles don’t have any neighboring mines. If there are adjacent blank tiles, all of them will be opened on the same click.
4. The numbers on uncovered tiles indicate the quantity of mines surrounding that tile.         
![Numbers](images/openedGrid.png) 
5. Right clicking a tile places a flag on it to help you track suspected mine locations. 
6. In order to win the game, you must uncover all tiles that don’t contain mines.
7. The game has two cheats to help you solve each puzzle. Can you find them?


## How to play

### Repl.it
The easiest way to play is on [repl.it](https://repl.it/talk/share/Minesweeper/84344). I recommend resizing the repl.it window a bit larger to improve your game play experience. When you're ready, click the `Run` button. The game takes a few seconds to load. If it doesn't, you may need to refresh the page.   

### Terminal   
The alternative approach has a better UI experience but requires some set-up:
1. Please install the latest version of [Python](https://www.python.org/downloads/)
2. Install pip and Pygame
  * Please use the following command in your terminal to check whether pip is installed: `python -m pip --version`. If not, navigate to [Pip](https://pip.pypa.io/en/stable/installing/) and complete the installation process.
  * Once pip is installed, please install the latest version of Pygame by typing the following into your terminal: `python3 -m pip install pygame`. If you have trouble installing Pygame, please visit Pygame's [Getting Started](https://www.pygame.org/wiki/GettingStarted) page.   
3. On GitHub, click the `Code` button in the Minesweeper repository. Download the zip files to your desktop and ensure the files are named `Minesweeper`.   
4. In your terminal type the following commands to navigate to the Minesweeper file folder:    
  * `cd Desktop`
  * `cd Minesweeper`
5. Enter `python3 Minesweeper.py` and begin playing.   

Thank you so much for visiting my project and happy gaming!




