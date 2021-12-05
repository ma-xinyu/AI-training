import torch
import numpy,cv2
from torchvision.datasets import MNIST  #数据集
from torchvision.transforms import Compose,ToTensor #转换操作
from torch.utils.data import DataLoader #批次数据集

def load_mnist(batch_size):
    train_data = MNIST(root="data",download=True,train=True,transform=Compose([ToTensor()]))
    vaild_data = MNIST(root="data",download=False,train=False,transform=Compose([ToTensor()]))

    train_loader = DataLoader(train_data,shuffle=True,batch_size=batch_size)
    vaild_loader = DataLoader(vaild_data,shuffle=True,batch_size=batch_size)
    return train_loader,vaild_loader