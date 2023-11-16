import tensorflow as tf
import numpy as np

print(tf.__version__)

# (x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_test = [[0], [1], [1], [0]]

# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.load_model("logic_gate_example")

validation_loss, validation_accuracy = model.evaluate(x_test, y_test)
print(validation_loss, validation_accuracy)

predictions = model.predict(x_test)

i = 3 # values from 0 to 3
result = np.argmax(predictions[i])

print("Outputs from neurons:")
for neuron, value in enumerate(predictions[i]):
    print(f"{neuron}: {round(value * 100, 2)}%")

print(f"The output of {x_test[i]} is {result} with an accuracy of {round(predictions[i][result] * 100, 2)}%")