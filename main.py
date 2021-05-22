import pygame
from pygame.locals import *
from pygame.surface import Surface

import colors
from Ball import Ball
from Brick import Brick
from Constants import *
from Player import Player

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

    brick_list = []
    number_of_lines = 8
    brick_y_position = top_limit_rect.bottom + 40
    line_value = 1000
    for i in range(number_of_lines):
        has_space = True
        margin_between_bricks = 8
        brick_x_position = left_limit_rect.right + margin_between_bricks / 2
        brick_y_position += 10
        brick_quantity = 0
        if i % 2 == 0 and i != 0:
            line_value -= 200
        while has_space:
            brick = Brick(brick_x_position, brick_y_position, line_value)
            brick_list.append(brick)
            brick_x_position += brick.rect.width
            brick_quantity += 1

            if brick_x_position >= right_limit_rect.left:
                has_space = False
            elif brick_x_position + margin_between_bricks >= right_limit_rect.left:
                has_space = False
            else:
                brick_x_position += margin_between_bricks

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

        for brick in brick_list:
            brick.render(window_surface)

        ball_1.render(window_surface)
        ball_1.update()
        ball_1.is_colliding_with_limits(right_limit_rect, left_limit_rect, top_limit_rect)
        ball_1.is_colliding_with_player(player_1)

        pygame.display.update()
