import tensorflow as tf

print(tf.__version__)

x_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [[0], [1], [1], [0]]

# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 8 neurons in the layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 8 neurons in the layer
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax)) # 2 neurons in the output layer (2 different possible results)

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=700)

model.save("logic_gate_example")

print("Model trained and saved.\nNow you can test it with tensorflow_predict.py!")