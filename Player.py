import pygame.image
from Constants import *


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(PLAYER_PADDLE_IMG_PATH)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - PLAYER_WIDTH/2, y)
        self.is_going_left = False
        self.is_going_right = False
        Player.life = 3
    def render(self, screen: pygame.surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def move(self, left_limit, right_limit):
        if self.is_going_left:
            self.rect.centerx -= 10
        elif self.is_going_right:
            self.rect.centerx += 10

        if self.rect.x <= left_limit:
            self.rect.x = left_limit
        elif self.rect.right >= right_limit:
            self.rect.right = right_limit
