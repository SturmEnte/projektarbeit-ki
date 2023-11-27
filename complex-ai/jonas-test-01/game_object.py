import pygame

class GameObject:

    def __init__(self, left, top, width, height, color, screen):
        self.rect = pygame.Rect(left, top, width, height)
        self.color = color
        self.screen = screen
        self.update_position_vars()

    def move(self, x, y):
        self.rect.move(x, y)
        self.update_position_vars()

    # def render(self):
    #     print(self.color)
    #     pygame.draw.rect(self.screen, self.color, self.rect)

    def update_position_vars(self):
        self.left = self.rect.width
        self.top = self.rect.top
        self.width = self.rect.width
        self.height = self.rect.height

    def colliderect(self, rect):
        return self.rect.colliderect(rect)