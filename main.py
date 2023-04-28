import pygame
from controls import *
from board.board import Board

# canvas setup
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyChess")

# object creation
board = Board(BOARD_WIDTH, BOARD_HEIGHT, (WIDTH - BOARD_WIDTH) // 2, (HEIGHT - BOARD_HEIGHT) // 2)

# app prep
board.create_board()


# main game loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        board.draw_board(win)
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()
