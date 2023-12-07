import tensorflow as tf

print(tf.__version__)

model = tf.keras.models.Sequential()

# x_train: [ [corner0_distance, corner0_y],  [corner1_distance, corner1_y] ]
# y_train: [  ]

x_train = [ [10, 0, 50, 0] ]
y_train = [ [1, 0] ]


model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) # 128 neurons in the layer
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax)) # 10 neurons in the output layer (10 different possible results)

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=1)

model.save("ai")