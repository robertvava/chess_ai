import pygame
from .constants import *


# Black pieces

b_king = pygame.transform.scale(pygame.image.load("images/black_king.png"), IMAGE_SIZE)
b_queen = pygame.transform.scale(pygame.image.load("images/black_queen.png"), IMAGE_SIZE)
b_bishop = pygame.transform.scale(pygame.image.load("images/black_bishop.png"), IMAGE_SIZE)
b_horse = pygame.transform.scale(pygame.image.load("images/black_horse.png"), IMAGE_SIZE)
b_tower = pygame.transform.scale(pygame.image.load("images/black_tower.png"), IMAGE_SIZE)
b_pawn = pygame.transform.scale(pygame.image.load("images/black_pawn.png"), IMAGE_SIZE)

# White pieces

w_king = pygame.transform.scale(pygame.image.load("images/white_king.png"), IMAGE_SIZE)
w_queen = pygame.transform.scale(pygame.image.load("images/white_queen.png"), IMAGE_SIZE)
w_bishop = pygame.transform.scale(pygame.image.load("images/white_bishop.png"), IMAGE_SIZE)
w_horse = pygame.transform.scale(pygame.image.load("images/white_horse.png"), IMAGE_SIZE)
w_tower = pygame.transform.scale(pygame.image.load("images/white_tower.png"), IMAGE_SIZE)
w_pawn = pygame.transform.scale(pygame.image.load("images/white_pawn.png"), IMAGE_SIZE)



