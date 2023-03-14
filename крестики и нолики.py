import pygame # pip install pygame
import random
import sys

pygame.init()

black = ( 0, 0, 0 )
white = ( 255, 255, 255 )
blue = ( 0, 0, 255 )
red = ( 255, 0, 0 )

side = 600
cell = 200

screen = pygame.display.set_mode( ( side, side ) )
pygame.display.set_caption( 'крестики и нолики' )

screen.fill( white )

board = [
    ['','',''],
    ['','',''],
    ['','',''],    
]

pygame.draw.line( screen, black, ( cell, 0 ), ( cell, side ), 5 )
pygame.draw.line( screen, black, ( cell * 2, 0 ), ( cell * 2, side ), 5 )
pygame.draw.line( screen, black, ( 0, cell ), ( side, cell ), 5 )
pygame.draw.line( screen, black, ( 0, cell * 2 ), ( side, cell * 2 ), 5 )

pygame.display.flip()

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()




















        
