import pygame
from controls import *
import numpy as np
from square import Square
from object import Object


class Board(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.squares = np.zeros((ROW_LENGTH, ROW_LENGTH), dtype=object)

    def create_board(self):
        for row in range(ROW_LENGTH):
            for column in range(ROW_LENGTH):
                square_color = LIGHT_SQUARE if (row + column) % 2 == 0 else DARK_SQUARE
                self.squares[row, column] = Square(square_color, column * self.width, row * self.height)

    def draw_board(self, win):
        for square in np.nditer(self.squares):
            square.draw(win)
