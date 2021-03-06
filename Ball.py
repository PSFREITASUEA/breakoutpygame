import pygame
from Constants import *


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.dx = 1
        self.dy = 1
        self.speed = 4

        # setting a max speed for ball speed increment
        self.max_speed = 10

    def is_colliding_with_brick(self):
        brick_list = []
        for brick in brick_list:
            if self.rect.colliderect(brick.rect):
                # makes the brick invisible after a collision
                brick.hide_brick()
                brick.increment_score()
                brick.remove(brick)
                # changes vertical direction and increases ball speed
                self.dy *= -1
                self.speed += 1

    def is_colliding_with_limits(self, right_limit_rect, left_limit_rect, top_limit_rect, player):

        if self.rect.colliderect(right_limit_rect) or self.rect.x > right_limit_rect.x:
            self.rect.x = right_limit_rect.x - 20
            self.dx *= -1
            pygame.mixer.Sound(BOUNCE_SFX_PATH).play()

        elif self.rect.colliderect(left_limit_rect) or self.rect.x > right_limit_rect.x:
            self.rect.x = left_limit_rect.x + 10
            self.dx *= -1

        elif self.rect.top <= top_limit_rect.bottom and self.dy < 0:
            self.dy *= -1

        elif self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.x = WINDOW_WIDTH / 2
            self.rect.y = WINDOW_HEIGHT / 2
            player.life -= 1

            # todo change death sound to something different
            pygame.mixer.Sound(BOUNCE_SFX_PATH).play()

    def is_colliding_with_player(self, player):
        if self.rect.colliderect(player.rect) and self.dy > 0:
            self.dy *= -1
            
            # reaction of the ball when it touches the right of the paddle
            if player.rect.right >= self.rect.centerx > (player.rect.centerx + 10):
                self.dx = 1

            # reaction of the ball when it touches the left of the paddle
            elif player.rect.left <= self.rect.centerx < (player.rect.centerx - 10):
                self.dx = -1

            # reaction of the ball when it touches the middle of the paddle
            elif (player.rect.centerx + 10) >= self.rect.centerx > (player.rect.centerx - 10):
                self.dx = 0

            pygame.mixer.Sound(BOUNCE_SFX_PATH).play()

    def update(self):
        self.rect.y += self.dy * self.speed / 2
        self.rect.x += self.dx * self.speed / 2

    def render(self, screen: pygame.surface):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
