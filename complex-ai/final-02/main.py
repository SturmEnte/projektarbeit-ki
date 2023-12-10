from game import Game
from threading import Thread
from time import sleep
import tensorflow as tf
import numpy as np

game = Game()
game_thread = Thread(target=game.start)
game_thread.start()

screen_width = 1280
screen_height = 720
standard_level = 100
player_width = 60
max_height_element = 150

moving_right = False

model = tf.keras.models.load_model("ai")

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
    #print(f"Distance to Object 0: {game.game_objects[0].rect.left}")
    sleep(0.1)
    
    predictions = model.predict([[touching_distance_normalized, touching_y_normalized, nearest_distance_normalized, nearest_y_normalized, player_y_normalized]]) # request prediction from model with normalized values
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