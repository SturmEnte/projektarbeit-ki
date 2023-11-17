import pygame
import time
import math

class Player:

    def __init__(self, screen):
        player_width = 60
        player_height = 100

        self.rect = pygame.Rect(screen.get_width() / 2 - player_width, screen.get_height() / 2 - player_height, player_width, player_height)
        self.screen = screen

        self.speed_x = 0
        self.speed_y = 0
        self.fall_start = time.time()
        self.falling = True

    def update(self):

        if self.falling:
            # Fall down like in real live (10 m/s² == 100 pixels/s²)
            self.speed_y = math.sqrt(2 * 100 * (time.time() - self.fall_start))

        self.rect.update(self.rect.left, self.rect.top + self.speed_y, self.rect.width, self.rect.height)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)