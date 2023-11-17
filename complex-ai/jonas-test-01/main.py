import pygame
from player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ground = pygame.Rect(0,screen.get_height() - 100 ,screen.get_width(), 100)

scroll_x = 0
scroll_y = 0

player = Player(screen)

player_colliders = [ground]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 128, 255))

    # Update

    for player_collider in player_colliders:
        player_collider.update(player_collider.left - scroll_x, player_collider.top - scroll_y, player_collider.width, player_collider.height)
        
        if player.rect.colliderect(player_collider):
            player.falling = False
            player.speed_y = 0
    
    player.update()
    
    # Render
    player.draw()
    for player_collider in player_colliders:
        pygame.draw.rect(screen, (255, 255, 255), player_collider)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()