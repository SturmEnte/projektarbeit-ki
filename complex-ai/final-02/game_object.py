import pygame

class GameObject:

    def __init__(self, left, top, width, height, color, screen, id=0):
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color
        self.screen = screen
        self.id = id
        self.update_position_vars()

    def move(self, x, y):
        self.rect.update(self.rect.left + x, self.rect.top + y, self.rect.width, self.rect.height)
        self.update_position_vars()

    def update_position_vars(self):
        self.left = self.rect.width
        self.top = self.rect.top
        self.width = self.rect.width
        self.height = self.rect.height

    def colliderect(self, rect):
        return self.rect.colliderect(rect)