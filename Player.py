import pygame.image


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/white_player.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def render_on_initial_position(self, screen: pygame.surface):
        screen.blit(self.image, (self.rect.x - self.rect.width / 2, self.rect.y))
