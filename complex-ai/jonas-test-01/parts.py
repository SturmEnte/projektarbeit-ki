from game_object import GameObject
from random import randrange as random
from utils import generate_id

class Parts:

    def __init__(self, s_width, s_height):
        # The first entry in a part is the width of the part
        # After that comes the most left game object of that part
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

        self.s_width = s_width

        self.spawned_parts = []

    def spawn_part_n(self, start_x, n, screen):
        part = self.parts[n]
        
        ids = []
        game_objects = []

        for i, object in enumerate(part):
            if i == 0:
                continue
            game_object = GameObject(object[0] + start_x, object[1], object[2], object[3], object[4], screen, generate_id(i))
            ids.append(game_object.id)
            game_objects.append(game_object)

        self.spawned_parts.append((part[0], ids))

        return game_objects

    def spawn_random_part(self, start_x, screen):
        n = random(0, len(self.parts))
        print(f"Spawned part {n}")
        return self.spawn_part_n(start_x, n, screen)
    
    def update(self, game_objects, screen):
        part = self.spawned_parts[len(self.spawned_parts) - 1]
        id = part[1][0]
        width = part[0]
        
        for game_object in game_objects:
            if game_object.id == id:
                if game_object.rect.left <= self.s_width:
                    return self.spawn_random_part(game_object.rect.left + width, screen)