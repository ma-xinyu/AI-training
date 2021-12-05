"""
    1.随机取一个值
    2.求这个值x在函数f中的导数
    3.根据导数的正负，对x进行加减
        x -= h * g
            h系数控制下降的速度：学习率
            g控制下降的方向
y = x ^ 2 -2 * x + 3
"""
import torch

#1.随便取一个x
x = torch.Tensor([5])
x.requires_grad = True

#2.循环
epoch = 10000
learn_rate = 0.001

for n in range(epoch):
    #2.做函数运算
    y = x**2 - 2*x + 3
    #3.求导
    y.backward()
    with torch.no_grad():
    #4.更新x
        x -= x.grad * learn_rate
        x.grad.zero_()  #导数清空

print(x.detach().clone().numpy())   #从求导环境剥离 克隆 张量变向量
print(y.detach().clone().numpy())   #如果不改，输出是 tensor([2.], grad_fn=<AddBackward0>)