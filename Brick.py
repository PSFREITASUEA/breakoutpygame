import pygame


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
