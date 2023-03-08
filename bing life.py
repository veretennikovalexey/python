import pygame, sys, random, copy

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BLACK = (255 ,255 ,255)
WHITE = (0 ,0 ,0)
CELL_SIZE = 20
CELLS_X = WINDOW_WIDTH // CELL_SIZE
CELLS_Y = WINDOW_HEIGHT // CELL_SIZE

def draw_grid(screen):
    for x in range(0 ,WINDOW_WIDTH ,CELL_SIZE):
        pygame.draw.line(screen ,WHITE ,(x ,0) ,(x ,WINDOW_HEIGHT))
    for y in range(0 ,WINDOW_HEIGHT ,CELL_SIZE):
        pygame.draw.line(screen ,WHITE ,(0 ,y) ,(WINDOW_WIDTH ,y))

def create_cells():
    cells = []
    for x in range(CELLS_X):
        column = []
        for y in range(CELLS_Y):
            if random.randint(0 ,1) == 0:
                column.append(False)
            else:
                column.append(True)
        cells.append(column)
    return cells

def draw_cells(screen ,cells):
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            if cells[x][y]:
                rect = pygame.Rect(x * CELL_SIZE ,y * CELL_SIZE ,CELL_SIZE ,CELL_SIZE)
                pygame.draw.rect(screen ,WHITE ,rect)

def update_cells(cells):
    new_cells = copy.deepcopy(cells)
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            neighbours = get_neighbours(x ,y ,cells)
            if cells[x][y] and (neighbours < 2 or neighbours > 3):
                new_cells[x][y] = False
            elif not cells[x][y] and neighbours == 3:
                new_cells[x][y] = True
    return new_cells

def get_neighbours(x,y,cells):
    neighbours=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==j==0:
                continue
            elif x+i<0 or x+i>=CELLS_X or y+j<0 or y+j>=CELLS_Y:
                continue
            elif cells[x+i][y+j]:
                neighbours+=1
    return neighbours

pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('The Life')
cells=create_cells()
FPS = 500
clock=pygame.time.Clock()

while True:
    screen.fill(BLACK)
    draw_grid(screen)
    draw_cells(screen,cells)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    
    cells=update_cells(cells)

clock.tick(FPS)
