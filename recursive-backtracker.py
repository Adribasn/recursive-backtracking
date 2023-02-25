import pygame, sys
import random
import time

screenSize = 550
rows = 50
cols = 50
cellSize = screenSize/rows
wallWidth = 1
screenSize = 550 + ((rows + 1) * wallWidth)
cellColor = (255, 255, 255)
wallColor = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
grid = []
stack = []
start_time = time.time()

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

        if head.x == updatedHead.x - 1 and updatedHead.y == head.y:
            #right
            pygame.draw.rect(screen, cellColor, ((head.x * cellSize) + ((head.x + 1) * wallWidth) + cellSize, (head.y * cellSize) + ((head.y + 1) * wallWidth), wallWidth, cellSize))
        elif head.x == updatedHead.x + 1 and updatedHead.y == head.y:
            #left
            pygame.draw.rect(screen, cellColor, ((head.x * cellSize) + ((head.x + 1) * wallWidth) - wallWidth, (head.y * cellSize) + ((head.y + 1) * wallWidth), wallWidth, cellSize))
        elif head.x == updatedHead.x and head.y == updatedHead.y - 1:
            #bottom
            pygame.draw.rect(screen, cellColor, ((head.x * cellSize) + ((head.x + 1) * wallWidth), (head.y * cellSize) + ((head.y + 1) * wallWidth) + cellSize, cellSize, wallWidth))
        elif head.x == updatedHead.x and head.y == updatedHead.y + 1:
            #top
            pygame.draw.rect(screen, cellColor, ((head.x * cellSize) + ((head.x + 1) * wallWidth), (head.y * cellSize) + ((head.y + 1) * wallWidth) - wallWidth, cellSize, wallWidth))
    
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            
            pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth), cellSize, cellSize))

    start = grid[0][0]
    finish = grid[-1][-1]

    pygame.draw.rect(screen, (0, 255, 0), ((start.x * cellSize) + ((start.x + 1) * wallWidth), (start.y * cellSize) + ((start.y + 1) * wallWidth), cellSize, cellSize))
    pygame.draw.rect(screen, (255, 0, 0), ((finish.x * cellSize) + ((finish.x + 1) * wallWidth), (finish.y * cellSize) + ((finish.y + 1) * wallWidth), cellSize, cellSize))
    
    if head.x == 0 and head.y == 0:
        print(str(time.time() - start_time) + ' time for maze to be generated')

    pygame.display.update()
    clock.tick(0)