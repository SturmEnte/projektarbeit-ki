import tensorflow as tf
import numpy as np
import cv2
from time import sleep

print(tf.__version__)

# let the user draw an image of a digit (0-9)

old_x = 0
old_y = 0
mouse_down = False

def draw(event, x, y, flags, parameters):
    global old_x, old_y, mouse_down, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_down = True
    
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_down = False
    
    elif event == cv2.EVENT_MOUSEMOVE and mouse_down:
        cv2.line(canvas, (old_x, old_y), (x, y), 255, thickness=2)
    
    old_x = x
    old_y = y

canvas = np.zeros((28, 28, 1), np.uint8)


window_name = "Draw an image of a digit (0-9)"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, canvas)
cv2.resizeWindow(window_name, 600, 600)
cv2.setMouseCallback(window_name, draw)

while True:
    cv2.imshow(window_name, canvas)
    key = cv2.waitKey(1)
    if key == 27 or key == 13:
        break  # esc or enter to predict drawn number
cv2.destroyAllWindows()
    

x_test = [canvas]

# x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.load_model("numbers_example")


predictions = model.predict(x_test)

result = np.argmax(predictions[0])

print("Outputs from neurons:")
for neuron, value in enumerate(predictions[0]):
    print(f"{neuron}: {round(value * 100, 2)}%")



print(f"The number is a {result} with an accuracy of {round(predictions[0][result] * 100, 2)}%")

img = x_test[0]
img = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()