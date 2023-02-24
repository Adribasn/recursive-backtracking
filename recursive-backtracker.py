import pygame, sys

#general
screenSize = 600

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()