import pygame
from pygame.locals import *
from pygame.surface import Surface

import colors
from Player import Player

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 1000
SCREEN_DIMENSION = (WINDOW_WIDTH, WINDOW_HEIGHT)

if __name__ == '__main__':
    window_surface: Surface = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.display.set_caption("BREAKOUT")

    running = True

    player_1 = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100)
    player_1.render_on_initial_position(window_surface)

    while running:
        # RECT(x,y,width,height)
        pygame.draw.rect(window_surface, colors.WHITE, (20, 20, 680, 30))
        pygame.draw.rect(window_surface, colors.WHITE, (20, 20, 10, 960))
        pygame.draw.rect(window_surface, colors.WHITE, (700, 20, 10, 970))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    print("Foi para a esquerda")
                elif event.key == K_d:
                    print("Foi para a direita")
            elif event.type == KEYUP:
                if event.key == K_a:
                    print("Parou de ir para esquerda")
                elif event.key == K_d:
                    print("Parou de ir para direita")

        pygame.display.flip()
