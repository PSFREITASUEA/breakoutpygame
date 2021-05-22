import pygame
from Constants import *


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.dx = 1
        self.dy = 1
        self.speed = 5

    def is_colliding_with_brick(self):
        # runs a check on every brick position
        brick_list = []
        for brick in brick_list:
            if self.rect.colliderect(brick.rect) and self.dy < 0:
                # makes the brick invisible after a collision
                brick.hide_brick()
                brick.increment_score()
                # changes vertical direction and increases ball speed
                self.dy *= -1
                self.speed += 5

                pygame.mixer.Sound(BOUNCE_SFX_PATH).play()

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
