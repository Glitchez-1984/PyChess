import pygame


class Piece(object):
    def __init__(self, width, height, x, y, img):
        super().__init__(width, height, x, y)
        self.img = img

    def draw(self, win):
        win.blit(self.img)
