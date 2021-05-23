import pygame
import colors


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
        self.rect = pygame.Rect(x, y, 30, 10)
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
        del self.rect

    def render(self, screen: pygame.surface):
        pygame.draw.rect(screen, self.color, self.rect)

    @staticmethod
    def is_colliding_with_ball(ball, brick_list):
        for brick in brick_list:
            if brick.rect.colliderect(ball.rect) and not brick.is_hidden:
                print(brick.rect)
                Brick.player_score += brick.value
                print(f"Points: {Brick.player_score}")
                ball.dy *= -1
                ball.speed += 1
