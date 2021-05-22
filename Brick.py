import pygame
player_score = 0


class Brick:
    def __init__(self, x, y, color):
        # x and y represents the coordinate where the brick will be placed
        self.rect = pygame.Rect(x, y, 20, 5)
        self.x = x
        self.y = y
        self.is_hidden = False
        self.color = color

    def increment_score(self):
        global player_score
        # points added depends on the brick color
        if self.color == "blue":
            player_score += 100
        elif self.color == "green":
            player_score += 200
        elif self.color == "yellow":
            player_score += 400
        elif self.color == "orange":
            player_score += 800
        elif self.color == "red":
            player_score += 1000

    def hide_brick(self):
        self.is_hidden = True
