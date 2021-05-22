import pygame

import colors

player_score = 0


def define_color(value):
    if value == 1000:
        return colors.RED
    elif value == 800:
        return colors.ORANGE
    elif value == 600:
        return colors.GREEN
    elif value == 400:
        return colors.YELLOW
    else:
        return colors.WHITE


class Brick:
    def __init__(self, x, y, value):
        # x and y represents the coordinate where the brick will be placed
        self.rect = pygame.Rect(x, y, 20, 5)
        self.x = x
        self.y = y
        self.value = value
        self.is_hidden = False
        self.color = define_color(self.value)

    def increment_score(self):
        global player_score
        # points added depends on the brick color
        player_score += self.value

    def hide_brick(self):
        self.is_hidden = True

    def render(self, screen: pygame.surface):
        pygame.draw.rect(screen, self.color, self.rect)
