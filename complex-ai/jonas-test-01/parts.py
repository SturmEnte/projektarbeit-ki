from game_object import GameObject
from random import randrange as random

class Parts:

    def __init__(self, s_width, s_height):
        self.parts = [
            [
                (0, s_height-100, s_width, 100, (255, 255, 255))
            ],
            [
                (0, s_height-100, s_width, 100, (255, 0, 255))
            ]
        ]

    def spawn_part(self, start_x, n, screen):
        part = self.parts[n]
        
        game_objects = []

        for object in part:
            game_objects.append(GameObject(object[0] + start_x, object[1], object[2], object[3], object[4], screen))

        return game_objects

    def spawn_random_part(self, start_x, screen):
        n = random(0, len(self.parts))
        print(f"Spawned part {n}")
        return self.spawn_part(start_x, n, screen)