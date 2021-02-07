# Game_of_life

This is a simple python implementation of the Game of life designed by John Horton Conway using the Pygame library.

Teh source code contains an initial configuration (which can be changed by the user) and also allows for the user to make changes in real time to affect how the "game" develops.

To execute it, simply navigate to the directory where the source code is, type `python GameOfLife.py` and hit Enter. You will be prompted with a grid containing some white squares (the initial configuration), where you can add new "cells" by left clicking on the squares of the grid. You can also (when there are static "cells") delete them by right clicking them.

By pressing `P` on your keyboard, you will pause the execution of the "game", that way you can add groups of cells to the board and then press `P` again to resume the execution. In the case that all cells die, you can also use this pause feature to add new ones to keep the "game" going.

Lastly and while being paused, pressing `C` on your keyboard will clear all the cells.
