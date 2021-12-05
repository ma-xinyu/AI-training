import torch
from torch.nn import CrossEntropyLoss   #可调用对象 损失函数
from torch.optim import Adam       #优化器，用途：更新w，b
from lenet5 import Lenet5
from datasets import load_mnist
import os

#获取模块的安装路径
current_dir = os.path.dirname(__file__)

class Lenet5Trainer:

    def __init__(self,epoch,lr):
        super(Lenet5Trainer,self).__init__()
        #判定是否支持GPU
        self.CUDA = torch.cuda.is_available()
        #生成一个模型参数
        self.mod_file = os.path.join(current_dir,"mods/lenet5.pt")
        #1.准备数据集
        self.train_loader,self.vaild_loader = load_mnist(batch_size=1000)
        #2.准备模型
        self.net = Lenet5()
        if self.CUDA:
            self.net = self.net.cuda()
        #-------------------
        if os.path.exists(self.mod_file):
            print("加载已有模型")
            state_dict = torch.load(self.mod_file)  #加载到缓冲
            self.net.load_state_dict(state_dict)    #加载到模型
        else:
            print("restart")
        #-------------------
        #3.超参数：学习率，训练轮数
        self.lr = lr
        self.epoch = epoch
        #4.准备对象：优化器，损失函数
        #   更新参数
        self.optimizer = Adam(self.net.parameters(),lr=self.lr)
        #   损失函数的对象
        self.loss_f = CrossEntropyLoss()

    def train_one(self):    #一轮的训练
        #批循环训练
        for x,y in self.train_loader:
            if self.CUDA:
                x = x.cuda()
                y = y.cuda()
            #预测
            y_ = self.net(x)
            #计算损失值
            loss = self.loss_f(y_,y)
            #求导
            loss.backward()
            #使用优化器更新权重参数
            self.optimizer.step()
            #导数清空
            self.optimizer.zero_grad()
            #print(F"\t损失:{loss:8.6f}")

    def train(self):
        print("start")
        for e in range(self.epoch):
            print(F"第{e:03d}轮训练")
            self.train_one()
            #-----------------------
            #获取所有的权重系数的字典
            state_dict = self.net.state_dict()
            torch.save(state_dict,self.mod_file)
            #-----------------------
            self.vaild()
            

    @torch.no_grad()    #装饰器 保证不会被求导跟踪

    def vaild(self):
        v_loss = 0.0    #累加损失值
        v_correct_num = 0.0
        v_total_num = 0
        for vx,vy in self.vaild_loader:
            if self.CUDA:
                vx = vx.cuda()
                vy = vy.cuda()
            #累加预测样本数
            v_total_num += len(vx)
            #预测  
            vy_ = self.net(vx)
            #计算为概率
            prob = torch.softmax(vy_,dim=1)
            #取出最大下标(预测结果)
            pred_y = torch.argmax(prob,dim=1)
            #用预测结果与实际标签对比，计算正确率，vy == pred_y 返回0/1
            v_correct_num += (vy == pred_y).float().sum()
            #累加损失值
            v_loss += self.loss_f(vy_,vy)

        print(F"\t损失值：{v_loss:8.6f}，正确率：{v_correct_num/v_total_num * 100:6.2f}")

if __name__ == "__main__":
    trainer = Lenet5Trainer(epoch=10,lr=0.0001)
    trainer.train()