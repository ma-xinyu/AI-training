#python_array
import numpy
import cv2

#解析表达式  [color,color,color,透明度]
#[x%255,y%255,(x+y)%255,128] 三通道 128是透明度
arr = [[[x%255,y%255,(x+y)%255,128] for x in range(500)] for y in range(500)]
print(arr)

img = numpy.array(arr)  #把python的list改为ndarray

cv2.imwrite("dd.png",img)