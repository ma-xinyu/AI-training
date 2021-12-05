import torch
from torchvision.datasets import MNIST  # 数据集
from torchvision.transforms import Compose, ToTensor # 转换操作
from torch.utils.data import DataLoader # 批次数据集
import numpy, cv2

# 1. 加载数据集
transform = Compose([ToTensor()])  # torch加载图像使用的是PIL图像库
train_data = MNIST(root="data", download=True, train=True,  transform=transform)
valid_data = MNIST(root="data", download=True, train=False, transform=transform) 
# Dataset: __len__
print(len(train_data), len(valid_data))
# Dataset: 下标运算
image, label = train_data[0]
print(image.shape, label)
# help(train_data)

# torch的图像格式： NCHW
# 保存图像
for i in  range(10):
    # 取图像
    image, label = valid_data[i]
    # 转换为opencv
    # 1. 转为numpy
    image = image.cpu().clone().numpy()
    # 2. 转为0-255
    image = image * 255
    # 3. 取整
    image = image.astype(numpy.uint8)
    # 4. 通道转为第三维
    image = image.transpose([1, 2, 0])
    # 5. 保存
    cv2.imwrite(F"img_{i}_{label}.png", image)

# 2. 转换为批次数据集
train_loader = DataLoader(train_data, batch_size=10, shuffle=True)
# DataLoader : __iter__
for images, labels in train_loader:
    print(images.shape)
    print(labels)
    break
