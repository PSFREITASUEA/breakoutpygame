import pygame
from pygame.locals import *
from pygame.surface import Surface

import colors
from Player import Player

WINDOW_WIDTH = 460
WINDOW_HEIGHT = 720
SCREEN_DIMENSION = (WINDOW_WIDTH, WINDOW_HEIGHT)

PLAYER_SCORE = 0

if __name__ == '__main__':
    window_surface: Surface = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.display.set_caption("BREAKOUT")

    pygame.mixer.init()
    pygame.mixer.music.load("assets/cheetahmen.wav")
    pygame.mixer.music.play(loops=-1)

    running = True

    player_1 = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 60)

    left_limit_rect = Rect(10, 10, 10, 700)
    right_limit_rect = Rect(440, 10, 10, 700)
    top_limit_rect = Rect(20, 10, 420, 20)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player_1.is_going_left = True
                elif event.key == K_d:
                    player_1.is_going_right = True
            elif event.type == KEYUP:
                if event.key == K_a:
                    player_1.is_going_left = False
                elif event.key == K_d:
                    player_1.is_going_right = False

        window_surface.fill(colors.BLACK)
        pygame.draw.rect(window_surface, colors.WHITE, left_limit_rect)
        pygame.draw.rect(window_surface, colors.WHITE, right_limit_rect)
        pygame.draw.rect(window_surface, colors.WHITE, top_limit_rect)

        player_1.move(left_limit_rect.right, right_limit_rect.left)
        player_1.render(window_surface)

        pygame.display.update()
