import pygame

class Player:

    def __init__(self, screen):
        player_width = 60
        player_height = 100

        self.rect = pygame.Rect(screen.get_width() / 2 - player_width, screen.get_height() / 2 - player_height, player_width, player_height)
        self.screen = screen
        
    
    def update(self):
        if self.rect.top + self.rect.height < 40:
            self.rect.update(self.rect.left, self.rect.top + 2, self.rect.width, self.rect.height)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)