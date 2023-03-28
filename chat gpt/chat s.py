# write snake using pygame

import pygame
import random

# initialize pygame
pygame.init()

# set up the display
width = 500
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# set up the snake
snake_size = 10
snake_speed = 15
snake_x = 250
snake_y = 250
snake_x_change = 0
snake_y_change = 0

# set up the food
food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

# set up the score
score = 0
font = pygame.font.SysFont(None, 25)

# game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0
    
    # update the snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change
    
    # check if the snake has collided with the wall
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        game_over = True
    
    # check if the snake has collided with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
        score += 1
    
    # draw the snake and food on the screen
    display.fill(black)
    pygame.draw.rect(display, red, [food_x, food_y, snake_size, snake_size])
    snake_head = [snake_x, snake_y]
    snake_list = [snake_head]
    pygame.draw.rect(display, white, [snake_x, snake_y, snake_size, snake_size])
    
    # update the score
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, [0, 0])
    
    # update the display
    pygame.display.update()
    
    # set the snake's speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# quit the game
pygame.quit()
quit()
