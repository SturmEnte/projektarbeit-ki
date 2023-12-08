from game import Game
from threading import Thread
from time import sleep
import tensorflow as tf
import numpy as np
from model import get_random_model
import sys

screen_width = 1280
screen_height = 720
standard_level = 100
player_width = 60

models = {}

def play_game(model):
    game = Game()
    game_thread = Thread(target=game.start)
    game_thread.start()
    
    moving_right = False

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
        #print(f"Touching Distance: {touching_distance}\nTouching y: {touching_y}\nNearest Distance: {nearest_distance}\nNearest y: {nearest_y}")
        #print(f"Distance to Object 0: {game.game_objects[0].rect.left}")
        
        predictions = model.predict([[touching_distance, touching_y, nearest_distance, nearest_y]])
        result = np.argmax(predictions[0])
        
        # player should stand still
        if result == 0:
            if moving_right:
                game.player.move_right(False)
                moving_right = False
        
        # player should move to the right
        elif result == 1:
            if not moving_right:
                game.player.move_right(True)
                moving_right = True
        
        # player should move to the right and jump
        elif result == 2:
            if not moving_right:
                game.player.move_right(True)
                moving_right = True
            game.player.jump()
        #print(f"Prediction: 0: {round(predictions[0][0], 2)}; 1: {round(predictions[0][1], 2)}")
        
        if game.game_over:
            models[model] = game.player.traveled_distance
            break
        
        sleep(0.1)


# first generation from random models (if requested)
if len(sys.argv) >= 2 and sys.argv[1] == "from_scratch":
    for i in range(20):
        model = get_random_model()
        play_game(model)
    print(models)
    best_model = None
    best_distance = 0
    for model in models:
        distance = models[model]
        if distance > best_distance:
            best_distance = distance
            best_model = model
    print(f"Best Model ({best_model}) reached a distance of {best_distance}!")
    best_model.save("ai")