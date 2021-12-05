import cv2

img = cv2.imread("import.png")
print(type(img))

cv2.imwrite("kong.png",img)