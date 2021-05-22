import pygame
import colors

from pygame.locals import *
from pygame.surface import Surface
from Player import Player
from Ball import Ball
from Constants import *


if __name__ == '__main__':
    window_surface: Surface = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.display.set_caption(WINDOW_CAPTION)

    pygame.mixer.init()
    pygame.mixer.music.load(BGM_PATH)
    pygame.mixer.music.play(loops=-1)

    running = True

    ball_1 = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    player_1 = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 60)

    # drawing screen borders
    left_limit_rect = Rect(10, 10, 10, 700)
    right_limit_rect = Rect(440, 10, 10, 700)
    top_limit_rect = Rect(20, 10, 420, 20)

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
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
        ball_1.render(window_surface)
        ball_1.update()
        ball_1.is_colliding_with_limits(right_limit_rect, left_limit_rect, top_limit_rect)
        pygame.display.update()
