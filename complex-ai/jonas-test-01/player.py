import pygame
import time

GRAVITY = 8
JUMP_FORCE = 15

class Player:

    def __init__(self, screen):
        player_width = 60
        player_height = 100

        self.rect = pygame.Rect(screen.get_width() / 2 - player_width / 2, screen.get_height() / 2 - player_height / 2, player_width, player_height)
        self.screen = screen

        self.speed_x = 0
        self.speed_y = 0
        self.speed_y_start = 0
        self.fall_start = time.time()
        self.falling = True
        self.relative_position = (0, 0)

    def update(self):
        if self.falling:
            # Fall down like in real live (10 m/s² == 10 pixels/s²)
            self.speed_y += GRAVITY * (time.time() - self.fall_start)

        self.relative_position = (self.relative_position[0] + self.speed_x, self.relative_position[1] + self.speed_y)
        self.rect.update(self.rect.left, self.rect.top + self.speed_y, self.rect.width, self.rect.height)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)

    def jump(self):
        if not self.falling:
            self.speed_y = -JUMP_FORCE
            self.falling = True
            self.fall_start = time.time()

    def move_left(self, should_move):
        if should_move:
            self.speed_x -= 10
        else:
            self.speed_x += 10

    def move_right(self, should_move):
        if should_move:
            self.speed_x += 10
        else:
            self.speed_x -= 10

    def get_scroll(self):
        return self.speed_x