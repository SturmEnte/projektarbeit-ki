import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = pygame.Rect(0, 0, 60, 100)
ground = pygame.Rect(0,screen.get_height() - 100 ,screen.get_width(), 100)

scroll_x = 0
scroll_y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 128, 255))

    # RENDER YOUR GAME HERE
    ground.update(ground.left - scroll_x, ground.top - scroll_y, ground.width, ground.height)
    
    if player.top + player.height < ground.top:
        player.update(player.left, player.top + 2, player.width, player.height)

    pygame.draw.rect(screen, (255, 0, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), ground)

    # scroll_x += 0.1

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()   