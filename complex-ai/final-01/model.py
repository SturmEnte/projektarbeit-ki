import tensorflow as tf
import numpy as np
from random import random

print(tf.__version__)

def get_random_model():
    model = tf.keras.models.Sequential()

    # x_train: [ corner0_distance, corner0_y, corner1_distance, corner1_y ]
    # y_train: [  ]

    x_train = [ [0, 0, 0, 0] ]
    y_train = [ [1] ]


    #model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
    model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax)) # 3 neurons in the output layer (0: nothing, 1: go right, 2: go right and jump)

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    #model.fit(x_train, y_train, epochs=1)
    model.predict(x_train)

    return model

def mutate(model, rate):
    for layer in model.layers:
        weights, biases = layer.get_weights() # not sure if the second array are the biases (all zeros?)
        new_weights = np.ndarray(weights.shape)
        for i, weight_list in enumerate(weights): # weight_lists contain arrays with the length of the current layers neurons and an amount of the previous layers neuron count
            for j, weight in enumerate(weight_list):
                if random() < rate:
                    weight += (random() / 5)
                new_weights[i][j] = np.float32(weight)
        layer.set_weights([new_weights, biases])

if __name__ == "__main__":
    model = get_random_model()
    model.save("random_ai")