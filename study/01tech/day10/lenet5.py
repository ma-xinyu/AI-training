import torch
from torch.nn import Module
from torch.nn import Conv2d, Linear
from torch.nn.functional import max_pool2d, relu  # 激活函数
from datasets import load_mnist

class Lenet5(Module):

    def __init__(self):
        super(Lenet5, self).__init__()
        # 定义有参数运算，主要目的就是初始化参数，设置为可求导
        self.conv1 = Conv2d(in_channels= 1, out_channels=  6, kernel_size=5, stride=1, padding=2)
        self.conv2 = Conv2d(in_channels= 6, out_channels= 16, kernel_size=5, stride=1, padding=0)
        self.conv3 = Conv2d(in_channels=16, out_channels=120, kernel_size=5, stride=1, padding=0)

        self.fc1 = Linear(120, 84)
        self.fc2 = Linear(84, 10) 


    def forward(self, x):
        # 定义运算过程
        y = x
        # ---------------1
        y = self.conv1(y)  # self.conv1.forward(y) # 可调用对象
        y = max_pool2d(y, (2, 2))
        y = relu(y, inplace=True)  # -的像素变成0：激活函数
        # ---------------2 1 * 6 * 14 * 16
        y = self.conv2(y)
        y = max_pool2d(y, (2, 2))
        y = relu(y, inplace=True)
        # ---------------3  1 * 16 * 5 *5
        y = self.conv3(y)
        y = relu(y, inplace=True)   # 1 * 120 * 1 * 1

        # 格式转换
        y = y.view(-1, 120)
        # --------------4
        y = self.fc1(y)
        y = relu(y, inplace=True)
        # --------------5
        y = self.fc2(y)  # 最后不需要激活
        return y

if __name__ == "__main__":     # 只有模块独立执行，才能被之心，被调用就执行不了
    net = Lenet5()
    # train, valid = load_mnist(batch_size=10)
    # for x, y in train:
    #     print("输入的形状：",x.shape)
    #     y_ = net(x)  # 预测值
    #     print("输出的形状：",y_.shape)
    #     # 转换为概率
    #     prob = torch.softmax(y_, dim=1)   # softmax == sigmoid 计算概率
    #     print(prob.detach().numpy())
    #     # 预测哪个数字
    #     cls_idx = torch.argmax(prob, dim=1)
    #     print(cls_idx.numpy()) 
    #     break
    # # 怎么训练？

    params = net.parameters()
    i = 0
    for param in params:
        print(i, param.requires_grad)
        i += 1




