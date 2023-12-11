from game_object import GameObject
from random import randrange as random
from utils import generate_id

DEFAULT_GROUND_HEIGHT = 100
DEFAULT_GROUND_COLOR = (255, 255, 255)

class Parts:

    part_sequence = [0, 2, 1, 2, 3, 0, 1, 3, 2, 2, 3, 0, 1, 2, 3, 2, 0, 3, 1]
    part_counter = 0

    def __init__(self, s_width, s_height):
        # The first entry in a part is the width of the part
        # After that comes the most left game object of that part
        self.parts = [
            # 3 short jumps
            [
                2 * 200 + 7 * 100,
                (0, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 1 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 3 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 5 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 7 * 100, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
            ],
            # 3 mid jumps
            [
                2 * 200 + 11 * 100,
                (0, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 2 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 5 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 8 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 11 * 100, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
            ],
            # 3 mid jumps up
            [
                2 * 200 + 10 * 100,
                (0, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 1.5 * 100, s_height - DEFAULT_GROUND_HEIGHT - 50, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 4.5 * 100, s_height - DEFAULT_GROUND_HEIGHT - 100, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 7.5 * 100, s_height - DEFAULT_GROUND_HEIGHT - 150, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 10 * 100, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
            ],
            # short - long - short
            [
                2 * 200 + 11 * 100,
                (0, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 1 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 5 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 9 * 100, s_height - DEFAULT_GROUND_HEIGHT, 100, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
                (200 + 11 * 100, s_height - DEFAULT_GROUND_HEIGHT, 200, DEFAULT_GROUND_HEIGHT, DEFAULT_GROUND_COLOR),
            ],
        ]


        # Test parts
        # self.parts = [
        #     [
        #         2 * s_width + 100,
        #         (0, s_height-100, s_width, 100, (255, 0, 255)),
        #         (s_width + 100, s_height - 100, s_width, 100, (255, 0, 255)),
        #         (2 * s_width + 100, s_height - 120, 10, 20, (255,0,255))
        #     ],
        #     [
        #         2 * s_width + 100,
        #         (0, s_height-100, s_width, 100, (0, 0, 255)),
        #         (s_width + 100, s_height - 100, s_width, 100, (0, 0, 255)),
        #         (2 * s_width + 100, s_height - 120, 10, 20, (0,0,255))
        #     ]
        # ]

        self.start_part = [
            s_width,
            (0, s_height-100, s_width, 100, (255, 255, 255))
        ]

        self.s_width = s_width

        self.spawned_parts = []

    def spawn_part_n(self, start_x, n, screen):
        part = self.parts[n]
        return self.spawn_part(start_x, part, screen)

    def spawn_random_part(self, start_x, screen):
        n = random(0, len(self.parts))
        print(f"Spawned part {n}")
        return self.spawn_part_n(start_x, n, screen)

    def spawn_part_from_sequence(self, start_x, screen):
        n = self.part_sequence[self.part_counter]
        self.part_counter += 1
        return self.spawn_part_n(start_x, n, screen)

    def spawn_part(self, start_x, part, screen):
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
    
    def spawn_start_part(self, screen):
        return self.spawn_part(0, self.start_part, screen)

    def update(self, game_objects, screen):
        part = self.spawned_parts[len(self.spawned_parts) - 1]
        id = part[1][0]
        width = part[0]
        
        for game_object in game_objects:
            if game_object.id == id:
                if game_object.rect.left <= self.s_width:
                    return self.spawn_part_from_sequence(game_object.rect.left + width, screen)