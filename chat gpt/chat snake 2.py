import pygame
import random

pygame.init()

width = 500
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption( "Snake Game" )

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

snake_size = 10
snake_speed = 15
snake_x = 250
snake_y = 250
snake_x_change = 0
snake_y_change = 0

food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

score = 0
font = pygame.font.SysFont(None, 25)

snake_list = []
snake_length = 1

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

	snake_x += snake_x_change
	snake_y += snake_y_change

	if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
		game_over = True

	snake_head = [snake_x, snake_y]
	snake_list.append(snake_head)
	if len(snake_list) > snake_length:
    		del snake_list[0]
    
	for segment in snake_list[:-1]:
    		if segment == snake_head:
        		game_over = True

	if snake_x == food_x and snake_y == food_y:
    		food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    		food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
    		snake_length += 1
    		score += 1

	display.fill(black)
	pygame.draw.rect(display, red, [food_x, food_y, snake_size, snake_size])

	for segment in snake_list:
		pygame.draw.rect(display, white, [segment[0], segment[1], snake_size, snake_size])

	text = font.render("Score: " + str(score), True, white)
	display.blit(text, [0, 0])

	pygame.display.update()

	clock = pygame.time.Clock()
	clock.tick(snake_speed)
pygame.quit()
quit()