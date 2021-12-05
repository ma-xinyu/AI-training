import torch
import cv2
import numpy
import os
from lenet5 import Lenet5

current_dir = os.path.dirname(__file__)


class Recognizer:

    def __init__(self):
        #创建模型
        self.net = Lenet5()
        #加载预训练模型
        self.mod_file = os.path.join(current_dir,"mods/lenet5.pt")
        #GPU支持
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.net = self.net.cuda()
        if os.path.exists(self.mod_file):
            state_dict = torch.load(self.mod_file)
            self.net.load_state_dict(state_dict)

    def pre_image(self,img):
        """
            假设图像是opencv，必须标准化，张量化
        """
        #把三通道转化为一通道 灰色图像
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #转为float
        img = img.astype(numpy.float32)
        #标准化
        img = img / 255.0
        #转化为张量
        img = torch.from_numpy(img).float().clone() #克隆 防止共用
        #转化为NCHW的格式：转为四维的格式
        img = img.view(-1,1,28,28)  #-1随便些，可以自己推导为1
        #GPU
        if self.CUDA:
            img = img.cuda()
        return img

    def recognize(self,img):
        #图像预处理
        img = self.pre_image(img)
        #预测
        y_ = self.net(img)
        #转为概率
        prob = torch.softmax(y_,dim=1)
        print(prob)     #概率向量
        #识别类型
        cls_idx = torch.argmax(prob,dim=1)
        #获取识别概率
        prob_idx = prob[0, cls_idx] #返回一个概率值

        #返回下标和概率 转cpu，剥离，元素只有一个可以用item
        return cls_idx.cpu().detach().item(), prob_idx.cpu().detach().item()


    def recognize_by_file(self,imgfile):
        img = cv2.imread(imgfile)
        return self.recognize(img)

if __name__ == "__main__":
    reco = Recognizer()
    idx,prob = reco.recognize_by_file("imgs/img_4_4.png")
    print(F"识别结果：{idx},概率：{prob}")