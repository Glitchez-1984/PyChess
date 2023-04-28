from object import Object
import pygame
from controls import *


class Square(Object):
    def __init__(self, color, x, y, width, height):
        super().__init__(width, height, x, y)
        self.color = color
        self.width = BOARD_WIDTH // ROW_LENGTH
        self.height = self.width
        self.square_object = pygame.Rect(self.x + SQUARE_SHIFT, self.y + SQUARE_SHIFT, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.square_object)
