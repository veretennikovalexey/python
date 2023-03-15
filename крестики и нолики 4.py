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

def check_winner() :
    for ii in range( 3 ):
        if board[ii][0] == board[ii][1] == board[ii][2] and board[ii][0] != '':
            return board[ii][0] 
        if board[0][ii] == board[1][ii] == board[2][ii] and board[0][ii] != '':
            return board[0][ii] 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None


def draw_board() :
    for row in range( 3 ):
        for col in range( 3 ):
            if board[ row ][ col ] == 'X':
                draw_x( row, col )
            if board[ row ][ col ] == 'O':
                draw_o( row, col )   

def is_board_full() :
    for row in range( 3 ):
        for col in range( 3 ):
            if board[ row ][ col ] == '':
                return False
    return True

# 0 1 2
# 1
# 2

def draw_o( row, col ) :
    pygame.draw.circle( screen, red, ( cell * col + cell // 2, cell * row + cell // 2 ), cell // 2 - 20, 10 )
    pygame.display.flip()

def draw_x( row, col ) :
    pygame.draw.line( screen, blue, ( col * cell + 20, row * cell + 20 ), ( cell * ( col + 1 ) - 20, cell * ( row + 1 ) - 20 ), 10 )
    pygame.draw.line( screen, blue, ( col * cell + 20, cell * ( row + 1 ) - 20 ), ( cell * ( col + 1 ) - 20, row * cell + 20 ), 10 )    
    pygame.display.flip()

# draw_o( 1, 1 )
# draw_x( 1, 1 )

def computer_move() :
    if is_board_full():
        return

    for row in range( 3 ):
        for col in range( 3 ):
            if board[ row ][ col ] == '':
                board[ row ][ col ] = 'O'
                if check_winner() == 'O':
                    return
                board[ row ][ col ] = ''

    for row in range( 3 ):
        for col in range( 3 ):
            if board[ row ][ col ] == '':
                board[ row ][ col ] = 'X'
                if check_winner() == 'X':
                    board[ row ][ col ] = 'O'
                    return
                board[ row ][ col ] = ''

    while True:
        row = random.randint( 0, 2 )
        col = random.randint( 0, 2 )
        if board[ row ][ col ] == '':
            board[ row ][ col ] = 'O'
            return
    

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_board_full() or check_winner() == 'O' or check_winner() == 'X':
                pygame.quit()
                sys.exit()
            row = event.pos[1] // cell    
            col = event.pos[0] // cell    
            if board[ row ][ col ] == '':
                board[ row ][ col ] = 'X'
                draw_board()
                if not check_winner() == 'X':
                    computer_move()
                    draw_board()    



















        
