# Minesweeper

This is my Pygame interpretation of the classic Windows game Minesweeper.

![Minesweeper](images/Minesweeper.gif)

## Game Rules
1. The first click is a freebie, you won't ever click on a mine.
2. The numbers displayed on each tile show the number of mines adjacent to it in a 3x3 grid. <br/>         
![Numbers](images/openedGrid.png) 
3. Right-click to place a flag over suspected mine locations. In order to win, you must clear all tiles except for the ones containing mines.   
4. There is a game cheat if you need help, it's an empty key, can you find it?

## How to play

### Repl.it
The easiest way to play is on [repl.it](https://repl.it/talk/share/Minesweeper/84316). I recommend resizing the repl.it window a bit larger to improve your game play experience. When you're ready, click the `Run` button.   

### Terminal   
The alternative approach for playing has a better UI experience but requires some set-up:
1. Please install the latest version of [Python](https://www.python.org/downloads/)
2. Install pip and Pygame
* Please use the following command in your terminal to check whether pip is installed: `python -m pip --version`. If not, navigate to [Pip](https://pip.pypa.io/en/stable/installing/) and complete the installation process.    
* Otherwise, please install the latest version of Pygame by typing the following into your terminal: `python3 -m pip install pygame`. If you have trouble installing Pygame, please visit Pygame's [Getting Started](https://www.pygame.org/wiki/GettingStarted) page.   
3. On GitHub, click the `Code` button in the Minesweeper repository. Download the zip files to your desktop and ensure the files are named `Minesweeper`.   
4. In your terminal type the following commands to navigate to the Minesweeper file folder:    
* `cd Desktop`
* `cd Minesweeper`
5. Enter `python3 Minesweeper.py` and begin playing.   

Thank you so much for visiting my project and happy gaming!




