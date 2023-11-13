import tensorflow as tf
import numpy as np
import cv2

print(tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.load_model("numbers_example")

validation_loss, validation_accuracy = model.evaluate(x_test, y_test)
print(validation_loss, validation_accuracy)

predictions = model.predict([x_test])

i = 0 # values from 0 to 9999
result = np.argmax(predictions[i])

print("Outputs from neurons:")
for neuron, value in enumerate(predictions[i]):
    print(f"{neuron}: {round(value * 100, 2)}%")

print(f"The number is a {result} with an accuracy of {round(predictions[i][result] * 100, 2)}%")

img = x_test[i]
img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_NEAREST)

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()