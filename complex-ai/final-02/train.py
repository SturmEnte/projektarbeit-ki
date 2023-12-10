from game import Game
from threading import Thread
from time import sleep
import tensorflow as tf
from model import get_random_model, mutate
from random import choice
import sys
import gc

screen_width = 1280
screen_height = 720
standard_level = 100
player_width = 60
max_height_element = 150

models_per_generation = 50
mutation_rate = 0.2
from_scratch = False
use_multithreading = False

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

def play_game(model, render_screen=True):
    game = Game()
    game_thread = Thread(target=game.start, args=(render_screen,))
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
        player_y = screen_height - standard_level - game.player.rect.bottom
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
        player_y_normalized = player_y / max_height_element # can be grater than 1 (might cause problems)
        #print(f"Touching Distance: {touching_distance}\nTouching y: {touching_y}\nNearest Distance: {nearest_distance}\nNearest y: {nearest_y}")
        #print(f"Normalized Values:\nTouching Distance: {touching_distance_normalized}\nTouching y: {touching_y_normalized}\nNearest Distance: {nearest_distance_normalized}\nNearest y: {nearest_y_normalized}")
        #print(f"Distance to Object 0: {game.game_objects[0].rect.left}")
        print(f"Player y: {player_y}\nPlayer y normalized: {player_y_normalized}")
        
        predictions = model.predict([[touching_distance_normalized, touching_y_normalized, nearest_distance_normalized, nearest_y_normalized, player_y_normalized]]) # request prediction from model with normalized values
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
    print("Training from scratch! This will delete the current best model.")
    answer = input("Are you sure you want to continue? y/n ")
    if "n" in answer or "N" in  answer:
        exit()
    print("Starting training from scratch...")
    from_scratch = True

if "parallel" in sys.argv:
    use_multithreading = True

while True:
    thread_list = []
    for i in range(models_per_generation):
        
        if from_scratch:
            model = get_random_model()
        else:
            model = tf.keras.models.load_model("ai")
            mutate(model, mutation_rate)
        
        if use_multithreading:
            thread_list.append(Thread(target=play_game, args=(model,False)))
            thread_list[-1].start()
        else:
            play_game(model)
        
    if use_multithreading:
        for thread in thread_list:
            thread.join()
    #print(models)
    best_model = None
    best_distance = 0
    for model in models:
        distance = models[model]
        if distance > best_distance:
            best_distance = distance
            best_model = model
    print(f"Best Model ({best_model}) reached a distance of {best_distance}!")
    best_model.save("ai")
    print("Saved current model!")
    print("Starting Next generation in 5 seconds...")
    sleep(5)
    del models
    gc.collect()
    models = {}
    from_scratch = False