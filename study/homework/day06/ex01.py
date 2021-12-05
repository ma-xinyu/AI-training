#img_io
import cv2

img = cv2.imread("import.png",cv2.IMREAD_COLOR)
print(type(img))
print(img.shape)    #三维数组：高height，宽wight，图像通道depth/channel

cv2.imwrite("kong.png",img)