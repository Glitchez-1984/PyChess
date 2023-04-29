import pygame
from controls import *
import numpy as np
from board.square import Square
from object import Object
from controls import *
from text import render_text

class Board(Object):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.squares = np.zeros((ROW_LENGTH, ROW_LENGTH), dtype=object)
        self.board = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))

    def create_board(self):
        for row in range(ROW_LENGTH):
            for column in range(ROW_LENGTH):
                square_color = LIGHT_SQUARE if (row + column) % 2 == 0 else DARK_SQUARE
                self.squares[row, column] = Square(square_color, column * SIDE, row * SIDE, SIDE, SIDE)

    def draw_board(self, win):
        win.blit(self.board, (self.x, self.y))
        nums = ['8','7','6','5','4','3','2','1']
        for square in self.squares.flat:
            square_surface = self.board.subsurface(square.square_object)
            square_surface.fill(square.color)
            pos = np.where(self.squares == square)
            if pos[1] == 0:
                render_text(square_surface, str(pos[0])[1],"arial",24,True,255,0,0,(255,0,0))
