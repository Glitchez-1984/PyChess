import pygame
import os
from controls import *
class Piece(object):
    def __init__(self, ptype, color):
        self.type = ptype
        self.color = color
        img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imgs', f"{self.color}{self.type}.svg"))
        self.image = pygame.transform.smoothscale(pygame.image.load(img_path), (SIDE, SIDE))
    def draw(self, win):
        win.blit(self.image,(0,0))
"s"