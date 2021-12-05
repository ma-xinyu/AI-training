import torch
import numpy
import cv2
from torchvision.datasets import MNIST  #数据集
from torchvision.transforms import Compose,ToTensor #转换操作
from torch.utils.data import DataLoader #批次数据集

#1.加载数据集
transform = Compose([ToTensor()])   #torch加载图像使用的是PIL图像库 img转换成张量
train_data = MNIST(root="data",download=True,train=True,transform=transform)    #训练集
vaild_data = MNIST(root="data",download=False,train=False,transform=transform)  #验证集
#Dataset类:__len__运算符
print(len(train_data),len(vaild_data))
#Dataset类:下标运算符
image,label = train_data[0]
print(image.shape,label)
#help(train_data)

#torch的图像格式：NCHW 数量 通道 高度 宽度（img：高 宽 通道）
#保存图像
for i in range(10):
    #取图像 取的是张量
    image,label = vaild_data[i]
    #转换为opencv
    #1.转为numpy
    image = image.cpu().clone().numpy() #在cpu上才能用numpy
    #2.转为0-255 像素是0-255
    image = image * 255
    #3.取整
    image = image.astype(numpy.uint8)
    #4.通道转为第三维 (把区别改变）
    image = image.transpose([1,2,0])
    #5.保存
    cv2.imwrite(F"img_{i}_{label}.png",image)   #label是手写数字


#2.转换为批次数据集
train_loader = DataLoader(train_data,batch_size=10,shuffle=True)  #一批10个
# DataLoader:__iter__
for images,labels, in train_loader:
    print(image.shape)
    print(labels)
    break