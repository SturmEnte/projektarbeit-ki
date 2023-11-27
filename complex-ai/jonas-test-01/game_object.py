import pygame

class GameObject:

    def __init__(self, left, top, width, height, color):
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color
        self.update_position_vars()

    def move(self, x, y):
        self.rect.move(x, y)
        self.update_position_vars()

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update_position_vars(self):
        self.left = self.rect.width
        self.top = self.rect.top
        self.width = self.rect.width
        self.height = self.rect.height

    def colliderect(self, rect):
        return self.rect.colliderect(rect)