import pygame
import time

GRAVITY = 8
JUMP_FORCE = 15

class Player:

    def __init__(self, screen):
        player_width = 60
        player_height = 100

        self.rect = pygame.Rect(screen.get_width() / 2 - player_width / 2, screen.get_height() / 2 - player_height / 2, player_width, player_height)
        self.ground_collider = pygame.Rect(self.rect.left, self.rect.top + player_height, self.rect.width, 1)
        self.side_colliders = [
            pygame.Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height),
            pygame.Rect(self.rect.left + self.rect.width + 1, self.rect.top, 1, self.rect.height)
        ]
        self.screen = screen

        self.speed_x = 0
        self.speed_y = 0
        self.speed_y_start = 0
        self.fall_start = time.time()
        self.falling = False
        self.traveled_distance = 0

    def update(self, game_objects):
        if self.falling:
            # Fall down like in real live (10 m/s² == 10 pixels/s²)
            self.speed_y += GRAVITY * (time.time() - self.fall_start)

        # x Movement        
        n = 1
        if self.speed_x < 0:
            n = -1
        elif self.speed_x == 0:
            n = 0
        
        #print(f"x-speed: {self.speed_x} \t| n: {n}")

        for _ in range(abs(round(self.speed_x))):
            b = False # Wether to break the loop
            for game_object in game_objects:
                if n == -1 and game_object.colliderect(self.side_colliders[0]):
                    b = True
                    break
                elif n == 1 and game_object.colliderect(self.side_colliders[1]):
                    b = True
                    break
            if b:
                break
            self.move(n, 0, game_objects)

        # y Movement
        n = 1
        if self.speed_y < 0:
            n = -1
        elif self.speed_y == 0:
            n = 0
        
        #print(f"y-speed: {self.speed_y} \t| n: {n}")

        for _ in range(abs(round(self.speed_y))):
            b = False # Wether to break the loop
            for game_object in game_objects:
                if n == 1 and game_object.colliderect(self.ground_collider):
                    b = True
                    break
            if b:
                break
            self.move(0, n, game_objects)

        #print(f"Travelled distance: {self.traveled_distance}") #!!!!!!!!!!!!!!!!!!!!!!!!!

    def move(self, left, top, game_objects):
        self.rect.update(self.rect.left, self.rect.top + top, self.rect.width, self.rect.height)
        self.ground_collider.update(self.ground_collider.left, self.ground_collider.top + top, self.ground_collider.width, self.ground_collider.height)
        for collider in self.side_colliders:
            collider.update(collider.left, collider.top + top, collider.width, collider.height)
        
        for game_object in game_objects:
            game_object.move(-left, 0)
        
        self.traveled_distance += left

    def draw(self, colliders=False):
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)

        if colliders == True:
            pygame.draw.rect(self.screen, (255, 0, 0), self.ground_collider) # Render ground collider of player
            for collider in self.side_colliders:
                pygame.draw.rect(self.screen, (255,0,0), collider)

    def jump(self):
        if not self.falling:
            self.speed_y = -JUMP_FORCE

    def move_left(self, should_move):
        if should_move:
            self.speed_x -= 10
        else:
            self.speed_x += 10

    def move_right(self, should_move):
        if should_move:
            self.speed_x += 10
        else:
            self.speed_x -= 10