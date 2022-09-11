from time import sleep
from src.constants import *
from game.board import *


# Set up pygame 
screen = SCREEN
pygame.init()
pygame.display.set_caption("Chess AI")
clock = pygame.time.Clock() 
time = 1
screen.fill((25, 25, 25))

# Set up class instances and game variables
board = Board()
running = True
left, middle, right = pygame.mouse.get_pressed()
 

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            mouse_coords = pygame.mouse.get_pos()
            tile_coords = convert_to_rowcol(mouse_coords[0], mouse_coords[1])            

            if left:
                print ("CLocked, for now. ")
                print (tile_coords)
                # print (mouse_coords[0])
    


    # Update screen
    pygame.display.flip()


# Quit game and close UI
pygame.quit()










































