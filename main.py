import pygame
from pygame.locals import *
from pygame.surface import Surface

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 1000
SCREEN_DIMENSION = (WINDOW_WIDTH, WINDOW_HEIGHT)

if __name__ == '__main__':
    window_surface: Surface = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.display.set_caption("BREAKOUT")
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
