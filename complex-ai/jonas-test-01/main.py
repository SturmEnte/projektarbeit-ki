import pygame
import time
from player import Player
from game_object import GameObject

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Variables
scroll_x = 0
scroll_y = 0

player = Player(screen)

game_objects = [
    GameObject(0, screen.get_height() - 100, screen.get_width(), 100, (255, 255, 255)),  # Ground
    GameObject(60, screen.get_height() - 140, 40, 40, (255, 255, 255 / 2))
]

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

    for game_object in game_objects:
        game_object.move(-scroll_x, -scroll_y)
        
        # Move the player out of the ground
        if player.rect.colliderect(game_object) and player.ground_collider.colliderect(game_object) and (player.side_colliders[0].colliderect(game_object) and player.side_colliders[1].colliderect(game_object)):

            while game_object.top < player.rect.top + player.rect.height:
                player.move(0, -1)

        # Move the player out of objects to its left
        if player.side_colliders[0].colliderect(game_object):
            while game_object.left + game_object.width > player.side_colliders[0].left:
                player.move(1, 0)
        
        # Move the player out of objects to its right
        if player.side_colliders[0].colliderect(game_object):
            while game_object.left < player.side_colliders[0].left + player.side_colliders[0].width:
                player.move(-1, 0)

        # Check if falling
        if game_object.colliderect(player.ground_collider):
            player.falling = False
            player.speed_y = 0
        else:
            if player.falling == False:
                player.falling = True
                player.fall_start = time.time()
    
    # Render game objects
    for game_obect in game_objects:
        game_object.render(screen)

    player.draw(colliders=True)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()