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
        if player.rect.colliderect(player_collider):
            player.falling = False
            player.speed_y = 0

    ground.update(ground.left - scroll_x, ground.top - scroll_y, ground.width, ground.height)
    
    player.update()
    
    # Render
    player.draw()
    pygame.draw.rect(screen, (255, 255, 255), ground)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()