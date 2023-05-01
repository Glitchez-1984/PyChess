import pygame
from controls import *
import numpy as np
from board.square import Square
from object import Object
from controls import *
from text import render_text
from board.piece import Piece
class Board(Object):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.squares = np.zeros((ROW_LENGTH, ROW_LENGTH), dtype=object)
        self.board = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        self.pieces = np.array([
    [Piece(3,"b"), Piece(1,"b"), Piece(2,"b"), Piece(4,"b"), Piece(5,"b"), Piece(2,"b"), Piece(1,"b"), Piece(3,"b")],
    [Piece(0,"b"), Piece(0,"b"), Piece(0,"b"), Piece(0,"b"), Piece(0,"b"), Piece(0,"b"), Piece(0,"b"), Piece(0,"b")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Piece(0,"w"), Piece(0,"w"), Piece(0,"w"), Piece(0,"w"), Piece(0,"w"), Piece(0,"w"), Piece(0,"w"), Piece(0,"w")],
    [Piece(3,"w"), Piece(1,"w"), Piece(2,"w"), Piece(4,"w"), Piece(5,"w"), Piece(2,"w"), Piece(1,"w"), Piece(3,"w")]
])

    def create_board(self):
        for row in range(ROW_LENGTH):
            for column in range(ROW_LENGTH):
                square_color = LIGHT_SQUARE if (row + column) % 2 == 0 else DARK_SQUARE
                self.squares[row, column] = Square(square_color, column * SIDE, row * SIDE, SIDE, SIDE)

    def draw_board(self, win):
        win.blit(self.board, (self.x, self.y))
        for square in self.squares.flat:
            square_surface = self.board.subsurface(square.square_object)
            square_surface.fill(square.color)
            pos = np.where(self.squares == square)
            piece = self.pieces[pos[0][0],pos[1][0]]
            if piece is not None:
                piece.draw(square_surface)
            if pos[1] == 0:
                render_text(square_surface, str(ROW_LENGTH - pos[0])[1],"Segoe UI Semibold",18,True,255,5,5,LIGHT_SQUARE if square.color == DARK_SQUARE else DARK_SQUARE, False)
            if pos[0] ==  ROW_LENGTH-1:
                render_text(square_surface, chr(int(str(pos[1])[1])+97), "Segoe UI Semibold", 18, True, 255, BOARD_WIDTH//ROW_LENGTH - 5, BOARD_HEIGHT//ROW_LENGTH -5,LIGHT_SQUARE if square.color == DARK_SQUARE else DARK_SQUARE, True)
