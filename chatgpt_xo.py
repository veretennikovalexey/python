import pygame
import random
import sys

# Инициализируем pygame
pygame.init()

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Определяем размеры окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 200

# Создаем окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Создаем доску
board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'

# Функция для рисования крестика
def draw_x(row, col):
    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + 20, row * CELL_SIZE + 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20), 10)
    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + 20, row * CELL_SIZE + CELL_SIZE - 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + 20), 10)

# Функция для рисования нолика
def draw_o(row, col):
    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 20, 10)

# Функция для рисования доски
def draw_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)

# Функция для проверки победителя
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

# Функция для проверки, все ли клетки заполнены
def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True

# Функция для хода компьютера
def computer_move():
    # Проверяем, есть ли выигрышный ход для компьютера
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'O'
                if check_winner() == 'O':
                    return
                board[row][col] = ''
    # Проверяем, есть ли выигрышный ход для человека
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
        # row = pygame.math.rand(0, 2)
        # col = pygame.math.rand(0, 2)
        row = random.randint( 0, 2 )
        col = random.randint( 0, 2 )

        if board[row][col] == '':
            board[row][col] = 'O'
            return

# Главный цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Ход человека
            if player == 'X':
                row = event.pos[1] // CELL_SIZE
                col = event.pos[0] // CELL_SIZE
                if board[row][col] == '':
                    board[row][col] = 'X'
                    player = 'O'
                    if check_winner() == 'X':
                        print("Победил игрок X!")
                        pygame.quit()
                        sys.exit()
                    elif is_board_full():
                        print("Ничья!")
                        pygame.quit()
                        sys.exit()
            # Ход компьютера
            if player == 'O':
                computer_move()
                player = 'X'
                if check_winner() == 'O':
                    print("Победил компьютер!")
                    pygame.quit()
                    sys.exit()
                elif is_board_full():
                    print("Ничья!")
                    pygame.quit()
                    sys.exit()
    # Отрисовка доски и фигур
    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()
