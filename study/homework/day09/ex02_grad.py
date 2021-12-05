import torch

x = torch.Tensor([1])

#设置x被求导
x.requires_grad = True

#进行函数运算，对x进行求导
y = x**3 + 3*x**2 - x*5 + 1
#避免运算被求导图跟踪
with torch.no_grad():
    z = y + 8*x
#求导
y.backward()
#z.backward()

#得到导数
print(x.grad)