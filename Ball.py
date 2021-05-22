import pygame
from Constants import *


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.dx = 1
        self.dy = 1
        self.speed = 4

    def is_colliding_with_brick(self):
        brick_list = []
        for brick in brick_list:
            if self.rect.colliderect(brick.rect) and self.dy < 0:
                # makes the brick invisible after a collision
                brick.hide_brick()
                brick.increment_score()
                # changes vertical direction and increases ball speed
                self.dy *= -1
                self.speed += 1


    def is_colliding_with_limits(self, right_limit_rect, left_limit_rect, top_limit_rect):
        if self.rect.right >= right_limit_rect.left or \
                self.rect.left <= left_limit_rect.right:
            self.dx *= -1

        elif self.rect.top <= top_limit_rect.bottom:
            self.dy *= -1

        elif self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.x = WINDOW_WIDTH / 2
            self.rect.y = WINDOW_HEIGHT / 2
            self.dy = -1
            # todo change sound to something different

    def is_colliding_with_player(self, player):
        if self.rect.colliderect(player.rect) and self.dy > 0:
            self.dy *= -1


    def update(self):
        self.rect.y += self.dy * self.speed / 2
        self.rect.x += self.dx * self.speed / 2

    def render(self, screen: pygame.surface):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
