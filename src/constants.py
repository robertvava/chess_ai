import pygame


# Colors
BLACK = (0, 0, 0)
GREY = (190,190,190)
DARK_BROWN = (75, 50, 15)
WOOD = (205,170,125)
WHITE = (255, 255, 255)

# Board and Game Constants
TILE_SIZE = int(1000/8)
WIDTH = 1000
HEIGHT = 1000
BOARD_SIZE = TILE_SIZE * 8
BOARD_ROW = (WIDTH-BOARD_SIZE)//2
BOARD_COL = int((HEIGHT / 2) - (BOARD_SIZE / 2))
IMAGE_SIZE = (TILE_SIZE, TILE_SIZE)
MARGIN = 2

# Screen based on constants
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TILE_SURFACE = pygame.Surface((TILE_SIZE, TILE_SIZE))

# Convert row col to pixels for pygame drawing.  
def convert_to_pixels(row, col):
    return BOARD_ROW + row * TILE_SIZE, BOARD_COL + col * TILE_SIZE

def convert_to_rowcol(x, y):
    return (int(x/100), int(y/100))

