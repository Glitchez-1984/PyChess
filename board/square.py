from object import Object
import pygame
import controls


class Square(Object):
    def __init__(self, color, x, y):
        super().__init__(x, y)
        self.color = color
        self.width = controls.BOARD_WIDTH // controls.ROW_LENGTH
        self.height = self.width
        self.square_object = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.square_object)
