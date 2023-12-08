import tensorflow as tf

print(tf.__version__)

def get_random_model():
    model = tf.keras.models.Sequential()

    # x_train: [ corner0_distance, corner0_y, corner1_distance, corner1_y ]
    # y_train: [  ]

    x_train = [ [0, 0, 0, 0] ]
    y_train = [ [0] ]


    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
    model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax)) # 3 neurons in the output layer (0: nothing, 1: go right, 2: go right and jump)

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=1)

    return model

if __name__ == "__main__":
    model = get_random_model()
    model.save("ai")