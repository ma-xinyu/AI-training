import cv2

img = cv2.imread("00016.png")
print(type(img))

cv2.imwrite("dd.png", img)
