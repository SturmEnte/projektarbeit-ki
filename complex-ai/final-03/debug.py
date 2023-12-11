from game import Game
from threading import Thread
from time import sleep

screen_width = 1280
screen_height = 720
standard_level = 100
player_width = 60
max_height_element = 150

def play_game():
    game = Game()
    game_thread = Thread(target=game.start)
    game_thread.start()
    
    moving_right = False

    standing_still_counter = 0

    while True:
        if game.initialized:
            break
        sleep(0.1)

    while True:
        touching_distance = 0
        touching_y = 0
        nearest_distance = 0
        nearest_y = 0
        for i, object in enumerate(game.game_objects):
            if object.rect.left >= screen_width / 2 + player_width / 2:
                nearest_distance = object.rect.left - screen_width / 2 + player_width / 2
                nearest_y = screen_height - standard_level - object.rect.top
                touching_distance = game.game_objects[i-1].rect.left + game.game_objects[i-1].rect.width - screen_width / 2 + player_width / 2
                touching_y = screen_height - standard_level - game.game_objects[i-1].rect.top
                break
        
        nearest_distance_normalized = nearest_distance / 900 + 0.5
        touching_distance_normalized = touching_distance / 900 + 0.5
        #print(f"Touching Distance: {touching_distance}\nTouching y: {touching_y}\nNearest Distance: {nearest_distance}\nNearest y: {nearest_y}")
        print(f"Normalized Values:\nTouching Distance: {touching_distance_normalized}\nTouching y: {touching_y / max_height_element}\nNearest Distance: {nearest_distance_normalized}\nNearest y: {nearest_y / max_height_element}")
        if touching_distance_normalized < 0 or touching_distance_normalized > 1:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Touching Distance:", touching_distance_normalized)
        if nearest_distance_normalized < 0 or nearest_distance_normalized > 1:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Nearest Distance:", nearest_distance_normalized)
        #print(f"Distance to Object 0: {game.game_objects[0].rect.left}")
        
        sleep(0.1)

play_game()