from game import Game
from threading import Thread
from time import sleep
import tensorflow as tf
from model import get_random_model, mutate
from random import choice
import sys

screen_width = 1280
screen_height = 720
standard_level = 100
player_width = 60
max_height_element = 150

models_per_generation = 10

models = {}

def max_or_rand(array):
    max = array[0]
    equal_indicies = []
    for i, element in enumerate(array):
        if element == max:
            equal_indicies.append(i)
        elif element > max:
            max = element
            equal_indicies = [i]
    return choice(equal_indicies)

def play_game(model):
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
        if nearest_distance_normalized > 1: # needed to correct values at game start
            nearest_distance_normalized = 1 # (distance at game start is out of standard range)
        touching_distance_normalized = touching_distance / 900 + 0.5
        if touching_distance_normalized > 1:
            touching_distance_normalized = 1
        nearest_y_normalized = nearest_y / max_height_element
        touching_y_normalized = touching_y / max_height_element
        #print(f"Touching Distance: {touching_distance}\nTouching y: {touching_y}\nNearest Distance: {nearest_distance}\nNearest y: {nearest_y}")
        #print(f"Normalized Values:\nTouching Distance: {touching_distance_normalized}\nTouching y: {touching_y_normalized}\nNearest Distance: {nearest_distance_normalized}\nNearest y: {nearest_y_normalized}")
        #print(f"Distance to Object 0: {game.game_objects[0].rect.left}")
        
        predictions = model.predict([[touching_distance / (screen_width / 2), touching_y / max_height_element, nearest_distance / (screen_width / 2), nearest_y / max_height_element]]) # request prediction from model with normalized values
        result = max_or_rand(predictions[0])

        print(f"0: {predictions[0][0]}  1: {predictions[0][1]}  2: {predictions[0][2]}")
        
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
        

        if game.player.speed_x == 0:
            standing_still_counter += 1
            if standing_still_counter >= 20: # standing still for longer than two seconds
                game.game_over = True
        else:
            standing_still_counter = 0
        
        sleep(0.1)


# first generation from random models (if requested)
if "from_scratch" in sys.argv:
    for i in range(models_per_generation):
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

while True:
    for i in range(models_per_generation):
        model = tf.keras.models.load_model("ai")
        mutate(model)
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