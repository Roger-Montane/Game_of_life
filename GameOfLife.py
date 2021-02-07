import pygame
import numpy as np
import time
from Constants import *

pygame.init()
pygame.display.set_caption('Game of Life')
screen = pygame.display.set_mode(WINDOW_SIZE)
background = 25, 25, 25
screen.fill(background)
clock = pygame.time.Clock()

board = np.zeros((CELLS_X, CELLS_Y))

board[5, 3] = 1
board[5, 4] = 1
board[5, 5] = 1

board[21, 21] = 1
board[22, 22] = 1
board[22, 23] = 1
board[21, 23] = 1
board[20, 21] = 1

done = False
paused = False
clear = False
while not done:
    newBoard = np.copy(board)
    screen.fill(background)
    time.sleep(0.1)

    event = pygame.event.get()
    for ev in event:
        if ev.type == pygame.QUIT:
            done = True
            pygame.quit()
            quit()

        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_p:
            paused = not paused

        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_c and paused:
            clear = True

        mouse_click = pygame.mouse.get_pressed()
        if sum(mouse_click):
            posX, posY = pygame.mouse.get_pos()
            cellX, cellY = int(np.floor(posX/SIZE_X)), int(np.floor(posY/SIZE_Y))
            newBoard[cellX, cellY] = not mouse_click[2]


    for x in range(0, CELLS_X):
        for y in range(0, CELLS_Y):
            if not paused:
                number_of_neighbours = (board[(x-1)%CELLS_X, (y-1)%CELLS_Y] +
                                        board[(x)%CELLS_X, (y-1)%CELLS_Y] + 
                                        board[(x+1)%CELLS_X, (y-1)%CELLS_Y] +
                                        board[(x-1)%CELLS_X, (y)%CELLS_Y] +
                                        board[(x+1)%CELLS_X, (y)%CELLS_Y] +
                                        board[(x-1)%CELLS_X, (y+1)%CELLS_Y] +
                                        board[(x)%CELLS_X, (y+1)%CELLS_Y] +
                                        board[(x+1)%CELLS_X, (y+1)%CELLS_Y])
                if board[x, y] == 0 and number_of_neighbours == 3:
                    newBoard[x, y] = 1
                elif board[x, y] == 1 and (number_of_neighbours < 2 or number_of_neighbours > 3):
                    newBoard[x, y] = 0
            if clear:
                newBoard = np.zeros((CELLS_X, CELLS_Y))
                clear = False
            poly = [(x     * SIZE_X, y     * SIZE_Y),
                    ((x+1) * SIZE_X, y     * SIZE_Y),
                    ((x+1) * SIZE_X, (y+1) * SIZE_Y),
                    (x     * SIZE_X, (y+1) * SIZE_Y)]
            if newBoard[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    board = np.copy(newBoard)
    pygame.display.flip()

pygame.quit()