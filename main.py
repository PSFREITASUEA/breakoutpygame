import pygame
from pygame.locals import *
from pygame.surface import Surface

import colors
from Player import Player

WINDOW_WIDTH = 460
WINDOW_HEIGHT = 720
SCREEN_DIMENSION = (WINDOW_WIDTH, WINDOW_HEIGHT)

PLAYER_SCORE = 0


class Brick:
    def __init__(self, x, y, color):
        # x and y represents the coordinate where the brick will be placed
        self.rect = pygame.Rect(x, y, 20, 5)
        self.x = x
        self.y = y
        self.is_hidden = False
        self.color = color

    def increment_score(self):
        global PLAYER_SCORE
        # points added depends on the brick color
        if self.color == "blue":
            PLAYER_SCORE += 100
        elif self.color == "green":
            PLAYER_SCORE += 200
        elif self.color == "yellow":
            PLAYER_SCORE += 400
        elif self.color == "orange":
            PLAYER_SCORE += 800
        elif self.color == "red":
            PLAYER_SCORE += 1000

    def hide_brick(self):
        self.is_hidden = True


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.dx = 1
        self.dy = 1
        self.speed = 5

    def is_colliding_with_brick(self):
        brick_list = []
        for brick in brick_list:
            if self.rect.colliderect(brick.rect) and self.dy < 0:
                # makes the brick invisible after a collision
                brick.hide_brick()
                brick.increment_score()
                # changes vertical direction and increases ball speed
                self.dy *= -1
                self.speed += 5

                pygame.mixer.Sound('assets/bounce.wav').play()

    def is_colliding_with_wall(self):
        pass

    def update(self):
        self.rect.y += self.dy * self.speed
        self.rect.x += self.dx * self.speed
        self.is_colliding_with_brick()
        self.is_colliding_with_wall()

    def restart_position(self):
        # restart ball position after it hits the bottom
        pass

    def render(self, screen: pygame.surface):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)


pygame.mixer.init()
pygame.mixer.music.load("assets/cheetahmen.wav")
pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    window_surface: Surface = pygame.display.set_mode(SCREEN_DIMENSION)
    pygame.display.set_caption("BREAKOUT")

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
