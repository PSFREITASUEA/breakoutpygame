import pygame.image


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/white_player.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.is_going_left = False
        self.is_going_right = False

    def render(self, screen: pygame.surface):
        screen.blit(self.image, (self.rect.x - self.rect.width / 2, self.rect.y))

    def move(self):
        if self.is_going_left:
            self.rect.centerx -= 1
        elif self.is_going_right:
            self.rect.centerx += 1
