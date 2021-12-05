#slice
import numpy
import cv2

img = cv2.imread("baiyu.png")

"""
支持的图像：bmp/jpg/png/gif/tiff
"""
#print(img[1])  # 取一行
#print(img[1, 1])  # 某行某列的一个像素
#print(img[1, 1, 1]) # 取某个像素的颜色通道（分量）

#img[100] = 255     #改一行像素
#img[100,100,0] = 255   #改第一个通道
#img[100,100] = [0,0,255]   #改点的三个分量

#img[slice(50,100),slice(50,100,2)] = 255
#表达式方式
img[200:800 , 200:800:3 , 0] = 255 #0表示第一个通道
#img[: , : , 0] = 0     #去蓝
#img[img > 100] = 0     #全部位置的全部通道像素大于100的，改为0
#img[img[: , : , 0] > 100] = 0   #全部位置的第一个通道（蓝色元素）大于100，就改为0

cv2.imwrite("dd.png",img)