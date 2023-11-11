import cv2

path = "img/test.jpg"

img = cv2.imread(path)
img = cv2.resize(img, (640, 480))

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()