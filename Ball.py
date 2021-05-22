import pygame
import Constants

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

    def is_colliding_with_limits(self, right_limit_rect, left_limit_rect, top_limit_rect):
        if self.rect.right >= right_limit_rect.left or \
                self.rect.left <= left_limit_rect.right:
            self.dx *= -1

        elif self.rect.top <= top_limit_rect.bottom:
            self.dy *= -1

        elif self.rect.bottom >= Constants.WINDOW_HEIGHT:
            self.rect.x = Constants.WINDOW_WIDTH / 2
            self.rect.y = Constants.WINDOW_HEIGHT / 2
            self.dy = -1

    def update(self):
        self.rect.y += self.dy * self.speed
        self.rect.x += self.dx * self.speed

    def render(self, screen: pygame.surface):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
