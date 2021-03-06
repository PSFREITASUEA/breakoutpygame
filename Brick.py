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
    player_score = 0

    def __init__(self, x, y, value):
        # x and y represents the coordinate where the brick will be placed
        self.rect = pygame.Rect(x, y, 30, 10)
        self.x = x
        self.y = y
        self.value = value
        self.color = define_color(self.value)

    def increment_score(self):
        # points added depends on the brick color
        Brick.player_score += self.value

    def render(self, screen: pygame.surface):
        pygame.draw.rect(screen, self.color, self.rect)

    @staticmethod
    def is_colliding_with_ball(ball, brick_list):
        for brick in brick_list:
            if brick.rect.colliderect(ball.rect):
                Brick.player_score += brick.value
                ball.dy *= -1
                brick_list.remove(brick)
                if ball.speed < ball.max_speed:
                    ball.speed += 0.5

                print(f"Collision: {brick.rect}")
                print(f"Ball speed: {ball.speed}")
                print("---------------------")
