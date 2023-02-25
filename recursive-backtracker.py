import pygame, sys
import random

screenSize = 550
rows = 10
cols = 10
cellSize = 55
wallWidth = 6
screenSize = 550 + ((rows + 1) * wallWidth)
cellColor = (255, 255, 255)
wallColor = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
grid = []
stack = []

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connectedNeighbours = [False, False, False, False]
        self.visited = False

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(Cell(i, j))
    
    grid.append(row)

stack.append(grid[0][0])
stack[-1].visited = True

screen.fill(wallColor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    head = stack[-1] 
    validNeighbours = []
    if head.x - 1 >= 0:
        if grid[head.x - 1][head.y].visited == False:
            validNeighbours.append(grid[head.x - 1][head.y])
    if head.x + 1 < rows:
        if grid[head.x + 1][head.y].visited == False:
            validNeighbours.append(grid[head.x + 1][head.y])
    if head.y - 1 >= 0:
        if grid[head.x][head.y - 1].visited == False:
            validNeighbours.append(grid[head.x][head.y - 1])
    if head.y + 1 < cols:
        if grid[head.x][head.y + 1].visited == False:
            validNeighbours.append(grid[head.x][head.y + 1])
    
    if len(validNeighbours) == 0:
        if len(stack) > 1:
            stack = stack[:-1]
    else:
        randomNeighbour = random.randint(0, len(validNeighbours) - 1)
        updatedHead = validNeighbours[randomNeighbour]
        grid[updatedHead.x][updatedHead.y].visited = True
        stack.append(updatedHead)


    
    
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            #drawing cell
            pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth), cellSize, cellSize))
            if head.x == cell.x and head.y == cell.y:
                pygame.draw.rect(screen, (255, 0, 0), ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth), cellSize, cellSize))
            '''
            #drawing open segments
            #left wall
            if cell.visited == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth) - wallWidth, (cell.y * cellSize) + ((col + 1) * wallWidth), wallWidth, cellSize))
            #right wall
            if cell.visited == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth) + cellSize, (cell.y * cellSize) + ((col + 1) * wallWidth), wallWidth, cellSize))
            #top wall
            if cell.visited == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth) - wallWidth, cellSize, wallWidth))
            #bottom wall
            if cell.visited == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth) + cellSize, cellSize, wallWidth))
            '''
    pygame.display.update()
    clock.tick(5)