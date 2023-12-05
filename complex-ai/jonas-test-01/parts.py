from game_object import GameObject
from random import randrange as random

class Parts:

    def __init__(self, s_width, s_height):
        self.parts = [
            [
                s_width,
                (0, s_height-100, s_width, 100, (255, 255, 255))
            ],
            [
                2 * s_width + 100,
                (0, s_height-100, s_width, 100, (255, 0, 255)),
                (s_width + 100, s_height-100, s_width, 100, (255, 0, 255))
            ]
        ]

        self.spawned_parts = []

    def spawn_part_n(self, start_x, n, screen):
        part = self.parts[n]
        
        ids = []
        game_objects = []

        for i, object in enumerate(part):
            if i == 0:
                continue
            game_object = GameObject(object[0] + start_x, object[1], object[2], object[3], object[4], screen)
            ids.append(game_object.id)
            game_objects.append(game_object)

        self.spawned_parts.append((part[0], ids))

        return game_objects

    def spawn_random_part(self, start_x, screen):
        n = random(0, len(self.parts))
        print(f"Spawned part {n}")
        return self.spawn_part_n(start_x, n, screen)