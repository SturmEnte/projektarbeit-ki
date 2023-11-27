import pygame
import time
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

player_colliders = [ground, pygame.Rect(60,screen.get_height() - 140 ,40, 40)]

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
        
        # Move the player out of the ground
        if player.rect.colliderect(player_collider) and player.ground_collider.colliderect(player_collider) and (player.side_colliders[0].colliderect(player_collider) and player.side_colliders[1].colliderect(player_collider)):

            while player_collider.top < player.rect.top + player.rect.height:
                player.move(0, -1)

        # Move the player out of objects to its left
        if player.side_colliders[0].colliderect(player_collider):
            while player_collider.left + player_collider.width > player.side_colliders[0].left:
                player.move(1, 0)
        
        # Move the player out of objects to its right
        if player.side_colliders[0].colliderect(player_collider):
            while player_collider.left < player.side_colliders[0].left + player.side_colliders[0].width:
                player.move(-1, 0)

        # Check if falling
        if player_collider.colliderect(player.ground_collider):
            player.falling = False
            player.speed_y = 0
        else:
            if player.falling == False:
                player.falling = True
                player.fall_start = time.time()
    
    # Center camera
    x_difference = (screen.get_width() / 2 - player.rect.width / 2) - player.rect.left
    y_difference = (screen.get_height() / 2 - player.rect.height / 2) - player.rect.top

    player.move(x_difference, 0)

    for collider in player_colliders:
        collider.move(x_difference, 0)
    
    for game_object in game_objects:
       game_object.update(game_object.left + x_difference, game_object.top + y_difference, game_object.width, game_object.height)
    

    # Render game objects
    for player_collider in player_colliders:
        pygame.draw.rect(screen, (255, 255, 255), player_collider)

    player.draw()
    
    pygame.draw.rect(screen, (255, 0, 0), player.ground_collider) # Render ground collider of player
    for collider in player.side_colliders:
        pygame.draw.rect(screen, (255,0,0), collider)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()