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

def draw_o( row, col ) :
    pygame.draw.circle( screen, red, ( cell * col + cell // 2, cell * row + cell // 2 ), cell // 2 - 20, 10 )
    pygame.display.flip()

def draw_x( row, col ) :
    pygame.draw.line( screen, blue, ( col * cell + 20, row * cell + 20 ), ( cell * ( col + 1 ) - 20, cell * ( row + 1 ) - 20 ), 10 )
    pygame.draw.line( screen, blue, ( col * cell + 20, cell * ( row + 1 ) - 20 ), ( cell * ( col + 1 ) - 20, row * cell + 20 ), 10 )    
    pygame.display.flip()

draw_o( 1, 1 )

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()




















        
