import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Define the colors of the chessboard
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a chessboard pattern using Pygame surfaces
board_size = (400, 400)
square_size = 50
chessboard = pygame.Surface(board_size)
for row in range(8):
    for col in range(8):
        x = col * square_size
        y = row * square_size
        color = WHITE if (row + col) % 2 == 0 else BLACK
        square = pygame.Surface((square_size, square_size))
        square.fill(color)
        chessboard.blit(square, (x, y))

# Load chess piece images onto the necessary chessboard squares
img_folder = "imgs/"
pieces = ["3", "1", "2", "4", "5", "2", "1", "3"]
for col, piece in enumerate(pieces):
    img_file = img_folder + "b" + piece + ".svg"
    img = pygame.image.load(img_file).convert_alpha()
    img = pygame.transform.scale(img, (square_size, square_size))
    chessboard.blit(img, (col * square_size, 0))
for col, piece in enumerate(pieces):
    img_file = img_folder + "b" + "0" + ".svg"
    img = pygame.image.load(img_file).convert_alpha()
    img = pygame.transform.scale(img, (square_size, square_size))
    chessboard.blit(img, (col * square_size, square_size))

# Blit the chessboard onto the screen
screen.blit(chessboard, (120, 40))

# Update the display to show the changes
pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
