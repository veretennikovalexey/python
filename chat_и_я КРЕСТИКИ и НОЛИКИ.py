import pygame
import random
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

SIDE = 600
CELL_SIZE = 200

screen = pygame.display.set_mode( ( SIDE, SIDE ) )
pygame.display.set_caption( "КРЕСТИКИ и НОЛИКИ" )

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

screen.fill( WHITE )
pygame.draw.line( screen, BLACK, ( CELL_SIZE, 0 ), ( CELL_SIZE, SIDE ), 5 )
pygame.draw.line( screen, BLACK, ( CELL_SIZE * 2, 0 ), ( 2 * CELL_SIZE, SIDE ), 5 )
pygame.draw.line( screen, BLACK, ( 0, CELL_SIZE ), ( SIDE, CELL_SIZE ), 5 )
pygame.draw.line( screen, BLACK, ( 0, CELL_SIZE * 2 ), ( SIDE, 2 * CELL_SIZE ), 5 )

pygame.display.flip()

def draw_x(row, col):
    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + 20, row * CELL_SIZE + 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20), 10)
    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + 20, row * CELL_SIZE + CELL_SIZE - 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + 20), 10)
    pygame.display.flip()

def draw_o(row, col):
    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 20, 10)
    pygame.display.flip()

def draw_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def computer_move():
    if is_board_full():
        return
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'O'
                if check_winner() == 'O':
                    return
                board[row][col] = ''
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'X'
                if check_winner() == 'X':
                    board[row][col] = 'O'
                    return
                board[row][col] = ''
    # Делаем случайный ход
    
    while True:
        row = random.randint( 0, 2 )
        col = random.randint( 0, 2 )
        if board[row][col] == '':
            board[row][col] = 'O'
            return    

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_board_full() or check_winner() == 'O':
                pygame.quit()
                sys.exit()                
            row = event.pos[1] // CELL_SIZE
            col = event.pos[0] // CELL_SIZE
            if board[row][col] == '':
                board[row][col] = 'X'
                draw_board()
                if not check_winner() == 'X':
                    computer_move()                
                    draw_board()
