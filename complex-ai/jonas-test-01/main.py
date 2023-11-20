import pygame
from player import Player

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Variables
ground = pygame.Rect(0,screen.get_height() - 100 ,screen.get_width(), 100)

scroll_x = 0
scroll_y = 0

player = Player(screen)

player_colliders = [ground]

# Game loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            
            if event.key == pygame.K_a:
                player.move_left(True)
            
            if event.key == pygame.K_d:
                player.move_right(True)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move_left(False)
            
            if event.key == pygame.K_d:
                player.move_right(False)    

    # Clear the screen
    screen.fill((0, 128, 255))

    # Update game objects
    player.update()

    scroll_x, _ = player.get_scroll()

    for player_collider in player_colliders:
        player_collider.update(player_collider.left - scroll_x, player_collider.top - scroll_y, player_collider.width, player_collider.height)
        
        if player.rect.colliderect(player_collider):

            while player_collider.top < player.rect.top + player.rect.height:
                player.move(0, -1)
                
        if player_collider.colliderect(player.ground_collider):
            player.falling = False
            player.speed_y = 0
        else:
            player.falling = True
    
    # Render game objects
    for player_collider in player_colliders:
        pygame.draw.rect(screen, (255, 255, 255), player_collider)

    player.draw()
    # pygame.draw.rect(screen, (255, 0, 0), player.ground_collider) # Render ground collider of player

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()