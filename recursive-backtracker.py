import pygame, sys
import random

#general
screenSize = 600
rows = 10
cols = 10
cellSize = screenSize/rows
grid = []
stack = []

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(Cell(i, j, 0))
    
    grid.append(row)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    if len(stack) == 0:
        while True:
            randRow = random.randint(0, rows-1)
            randCol = random.randint(0, cols-1)
            if randRow == 0 or randRow == rows-1:
                break
            elif randCol == 0 or randCol == cols-1:
                break

        currentCell = grid[randRow][randCol]
        currentCell.value = .5
        stack.append(currentCell)
    else:
        currentCell = stack[-1]
    
    validNeighbours = []

    if currentCell.x - 1 >= 0:
        if grid[currentCell.x - 1][currentCell.y].value == 0:
            validNeighbours.append(grid[currentCell.x - 1][currentCell.y])
    if currentCell.x + 1 < rows:
        if grid[currentCell.x + 1][currentCell.y].value == 0:
            validNeighbours.append(grid[currentCell.x + 1][currentCell.y])
    if currentCell.y - 1 >= 0:
        if grid[currentCell.x][currentCell.y - 1].value == 0:
            validNeighbours.append(grid[currentCell.x][currentCell.y - 1])
    if currentCell.y + 1 < cols:
        if grid[currentCell.x][currentCell.y + 1].value == 0:
            validNeighbours.append(grid[currentCell.x][currentCell.y + 1])

    if len(validNeighbours) > 0:
        randomNeighbourCount = random.randint(0, len(validNeighbours) - 1)
        updatedCurrentCell = validNeighbours[randomNeighbourCount]
        updatedCurrentCell.value = .5
        stack.append(validNeighbours[randomNeighbourCount])

        for i in range(currentCell.x - 1, currentCell.x + 2):
            if i >= 0 and i < rows:
                for j in range(currentCell.y - 1, currentCell.y + 2):
                    if j >= 0 and j < cols:
                        if grid[i][j].value != .5:
                            if i != updatedCurrentCell.x and j != updatedCurrentCell.y:
                                grid[i][j].value = 1
    else:
        currentCell.value = 1
        
    for row in grid:
        for cell in row:
            if cell.value == 0 or cell.value == .5:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, ((cell.x * cellSize, cell.y * cellSize), (cellSize, cellSize)))
    
    #pygame.draw.rect(screen, (255, 0, 0), ((currentCell.x * cellSize, currentCell.y * cellSize), (cellSize, cellSize)))
    pygame.display.update()
    clock.tick(5)