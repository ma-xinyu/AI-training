import torch
from torch.nn import Module
from torch.nn import Conv2d, Linear #卷积运算 线性运算
from torch.nn.functional import max_pool2d, relu    #磁化运算（磁化函数）  修正线性（改为正）（激活函数）
from datasets import load_mnist

class Lenet5(Module):

    def __init__(self):
        super(Lenet5,self).__init__()
        #定义有参数运算，主要目的就是初始化参数，设置为可求导
        #卷积运算
        #stride步数 padding补边
        self.conv1 = Conv2d(in_channels = 1,out_channels = 6,kernel_size = 5,stride = 1,padding = 2)    #变成28-5+1=24 为了变回28 各要补两个边 
        self.conv2 = Conv2d(in_channels = 6,out_channels = 16,kernel_size = 5,stride = 1,padding = 0)
        self.conv3 = Conv2d(in_channels = 16,out_channels = 120,kernel_size = 5,stride = 1,padding = 0)

        #全连接
        self.fc1 = Linear(120,84)
        self.fc2 = Linear(84,10)

    def forward(self,x):
        #定义运算过程
        y = x
        #------------第一层卷积
        y = self.conv1(y)   #self.conv1.forward(y) #可调用对象 #28x28
        #磁化 降维
        y = max_pool2d(y,(2,2)) #14x14
        y = relu(y,inplace=True) #把负的像素变为0：激活像素
        #------------第二层卷积
        y = self.conv2.forward(y)   #10x10
        y = max_pool2d(y,(2,2))     #5x5
        y = relu(y,inplace=True)
        #------------第三层卷积
        y = self.conv3.forward(y)   #1x1
        #卷成一个像素了，不能磁化了
        y = relu(y,inplace=True)

        #格式转换
        #120个特征变为10个特征 0，1，2...分别给出一个概率值
        y = y.view(-1,120)  #-1不管，自动推导  120是120个特征
        #------------第四层全连接
        y = self.fc1(y)
        y = relu(y,inplace=True)
        #------------第五层全连接
        y = self.fc2(y)
        #最后一个不用激活了

        return y

net = Lenet5()
train_loader,vaild_loader = load_mnist(batch_size=10)
for x,y in train_loader:
    print("输入：",x.shape)
    y_ = net(x) #预测值
    print("输出：",y_.shape)
    #转换成概率
    prob = torch.softmax(y_,dim=1)      #dim=1 概率之和为1
    print(prob.detach().numpy())
    #预测数字
    cls_idx = torch.argmax(prob, dim=1) #取概率最大的下标
    print(cls_idx.numpy()) 
    break