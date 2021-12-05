from sklearn.datasets import load_iris
import numpy
import torch

# 加载数据集
data, target = load_iris(return_X_y=True)

# x = torch.from_numpy(data[0:100]).float()
x = torch.Tensor(data[:100])   # FloatTensor = Tensor
y = torch.Tensor(target[:100]).view(100, 1)
# 定义学习参数
w = torch.randn(1, 4)
b = torch.randn(1)

w.requires_grad= True
b.requires_grad= True
# 超参数
epoch = 500000
lr = 0.0001

for n in range(epoch):
    # 预测
    # y_ = w @ x.T + b
    y_ = torch.nn.functional.linear(x, weight=w, bias=b)
    y_ = torch.sigmoid(y_)
    # 计算损失
    loss = torch.nn.functional.binary_cross_entropy(y_, y)
    # 求导
    loss.backward()
    # 更新
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
        # 清空导数
        w.grad.zero_()
        b.grad.zero_()
        
        y_[ y_ >  0.5] = 1
        y_[ y_ <= 0.5] = 0
        
        corr_rate = (y == y_).float().mean()
    if n % 100 ==0:
        print(f"损失值：{loss:8.6f}, 正确率：{corr_rate * 100: 8.2f}")