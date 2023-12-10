import pygame
import time
from player import Player
from game_object import GameObject
from parts import Parts
import os

class Game():
    initialized = False
    def start(self, render_screen=True):
        if not render_screen:
            os.environ["SDL_VIDEODRIVER"] = "dummy"

        # Pygame setup
        pygame.init()
        
        screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Jump'n'run Game | Projektarbeit (With AI)")
        clock = pygame.time.Clock()
        running = True

        # Variables
        scroll_x = 0
        scroll_y = 0
        self.game_over = False

        self.player = Player(screen)
        print(self.player)

        part_manager = Parts(screen.get_width(), screen.get_height())

        self.game_objects = []
        for game_object in part_manager.spawn_start_part(screen):
            self.game_objects.append(game_object)

        # Game loop
        while running:
            self.initialized = True
            # Poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    
                    if event.key == pygame.K_a:
                        self.player.move_left(True)
                    
                    if event.key == pygame.K_d:
                        self.player.move_right(True)

                    if event.key == pygame.K_g:
                        self.game_objects.append(GameObject(screen.get_width() / 2 + 10, screen.get_height() - 120, 100, 100, (0, 255, 0), screen))
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player.move_left(False)
                    
                    if event.key == pygame.K_d:
                        self.player.move_right(False)    

            # Clear the screen
            screen.fill((0, 128, 255))

            # Update game objects
            self.player.update(self.game_objects)

            collided_with_ground = False

            for game_object in self.game_objects:
                #game_object.move(-scroll_x, -scroll_y)
                
                # Move the player out of the ground
                if game_object.colliderect(self.player.rect) and game_object.colliderect(self.player.ground_collider) and game_object.colliderect(self.player.side_colliders[0]) and game_object.colliderect(self.player.side_colliders[1]):
                    while game_object.colliderect(self.player.rect):
                        self.player.move(0, -1)

                # Check for ground collision for falling mechanic
                if self.player.ground_collider.colliderect(game_object.rect):
                    collided_with_ground = True

            # Check if falling
            if collided_with_ground:
                if self.player.falling == True:
                    self.player.falling = False
                    self.player.speed_y = 0
                    print("Stopped falling: " + time.time().__str__())
            else:
                if self.player.falling == False:
                    self.player.falling = True
                    self.player.fall_start = time.time()
                    print("Started falling: " + time.time().__str__())

            if self.player.rect.top >= screen.get_height() + self.player.rect.height:
                print("Game Over")
                self.game_over = True
                #pygame.quit()
                print("break")
                break

            # Spawn new parts
            new_game_objects = part_manager.update(self.game_objects, screen)
            if new_game_objects:
                for game_object in new_game_objects:
                    self.game_objects.append(game_object)

            # Render game objects
            for game_object in self.game_objects:
                pygame.draw.rect(screen, game_object.color, game_object.rect)

            self.player.draw(colliders=True)

            # Display the game over text
            if self.game_over:
                font = pygame.font.SysFont(None, 100)
                text_surface = font.render("Game Over", True, (255, 0, 0))
                text_width, text_height = text_surface.get_size()
                text_center_x = screen.get_width() // 2 - text_width // 2
                text_center_y = screen.get_height() // 2 - text_height // 2
                screen.blit(text_surface, (text_center_x, text_center_y))
                #pygame.quit()
                break

            # FPS display
            fps_text = f"FPS: {int(clock.get_fps())}"
            font = pygame.font.Font(None, 24)
            fps_surface = font.render(fps_text, True, (0, 0, 255))
            screen.blit(fps_surface, (0, 0))

            pygame.display.flip()
            clock.tick(60)

        self.initialized = False
        #pygame.quit()