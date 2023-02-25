import pygame, sys

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

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connectedNeighbours = [False, False, False, False]

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(Cell(i, j))
    
    grid.append(row)

screen.fill(wallColor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    grid[5][5].connectedNeighbours[0] = True
    grid[5][5].connectedNeighbours[1] = True
    grid[5][5].connectedNeighbours[2] = True
    grid[5][5].connectedNeighbours[3] = True
            
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            #drawing cell
            pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth), cellSize, cellSize))

            #drawing open segments
            #left wall
            if cell.connectedNeighbours[0] == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth) - wallWidth, (cell.y * cellSize) + ((col + 1) * wallWidth), wallWidth, cellSize))
            #right wall
            if cell.connectedNeighbours[1] == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth) + cellSize, (cell.y * cellSize) + ((col + 1) * wallWidth), wallWidth, cellSize))
            #top wall
            if cell.connectedNeighbours[2] == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth) - wallWidth, cellSize, wallWidth))
            #bottom wall
            if cell.connectedNeighbours[3] == True:
                pygame.draw.rect(screen, cellColor, ((cell.x * cellSize) + ((row + 1) * wallWidth), (cell.y * cellSize) + ((col + 1) * wallWidth) + cellSize, cellSize, wallWidth))
    
    pygame.display.update()
    #clock.tick(5)