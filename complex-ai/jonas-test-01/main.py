import pygame
import time
from player import Player
from game_object import GameObject

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jump'n'run Game | Projektarbeit (Without AI)")
clock = pygame.time.Clock()
running = True

# Variables
scroll_x = 0
scroll_y = 0

player = Player(screen)

game_objects = [
    GameObject(0, screen.get_height() - 100, screen.get_width(), 100, (255, 255, 255), screen),  # Ground
    GameObject(60, screen.get_height() - 140, 100, 40, (255, 255, 255 / 2), screen),
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
    player.update(game_objects)

    scroll_x, _ = player.get_scroll()

    collided_with_ground = False

    for game_object in game_objects:
        game_object.move(-scroll_x, -scroll_y)
        
        # Move the player out of the ground
        if game_object.colliderect(player.rect) and game_object.colliderect(player.ground_collider) and game_object.colliderect(player.side_colliders[0]) and game_object.colliderect(player.side_colliders[1]):
            while game_object.colliderect(player.rect):
                player.move(0, -1)

        # Move the player out of objects to its left
        # if player.side_colliders[0].colliderect(game_object.rect):
        #     while game_object.left + game_object.width > player.side_colliders[0].left:
        #         player.move(1, 0)
        
        # Move the player out of objects to its right
        # if player.side_colliders[0].colliderect(game_object.rect):
        #     while game_object.left < player.side_colliders[0].left + player.side_colliders[0].width:
        #         player.move(-1, 0)

        # Check for ground collision for falling mechanic
        if player.ground_collider.colliderect(game_object.rect):
            collided_with_ground = True

    # Check if falling
    if collided_with_ground:
        if player.falling == True:
            player.falling = False
            player.speed_y = 0
            print("Stopped falling: " + time.time().__str__())
    else:
        if player.falling == False:
            player.falling = True
            player.fall_start = time.time()
            print("Started falling: " + time.time().__str__())
    
    # Move "camera"
    difference = player.get_x_offset(screen.get_width())

    print(f"Difference: {difference}")

    for game_object in game_objects:
        game_object.move(-difference, 0)

    # Render game objects
    for game_obect in game_objects:
        # The render function does not work for some reason. This way it works so this is an issue for later
        # game_object.render()
        pygame.draw.rect(screen, game_obect.color, game_obect.rect)

    player.draw(colliders=True)

    fps_text = f"FPS: {int(clock.get_fps())}"
    font = pygame.font.Font(None, 24)
    fps_surface = font.render(fps_text, True, (0, 0, 255))
    screen.blit(fps_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()