import tensorflow as tf

print(tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) # 10 neurons in the output layer (10 different possible results)

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=3)

model.save("numbers_example")

print("Model trained and saved.\nNow you can test it with tensorflow_predict.py!")