import torch
import cv2
import numpy
import os
from lenet5 import Lenet5

current_dir = os.path.dirname(__file__)

class Recognizer:

    def __init__(self):
        # 创建模型
        self.net = Lenet5()
        # 加载预训练模型 
        self.mod_file =  os.path.join(current_dir, "mods/lenet5.pt")
        # GPU支持
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.net = self.net.cuda()
        if os.path.exists(self.mod_file):
            state_dict = torch.load(self.mod_file)
            self.net.load_state_dict(state_dict)
        

    def pre_image(self, img):
        """
            假设图像是 opencv，必须标准化，张量化
        """
        # 把3通道转换为1通道
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 转为float
        img = img.astype(numpy.float32)
        # 标准化
        img = img / 255.0
        # 转换为张量
        img = torch.from_numpy(img).float().clone()
        # 转换为NCHW的格式：转为4维的格式
        img = img.view(-1, 1, 28, 28)
        # GPU
        if self.CUDA:
            img = img.cuda()
        return img

    def recognize(self, img):
        # 图像预处理
        img = self.pre_image(img)
        # 预测
        y_ = self.net(img)
        # 转为概率
        prob = torch.softmax(y_, dim=1)
        print(prob)  # 概率向量
        # 识别类型
        cls_idx = torch.argmax(prob, dim=1)
        # 获取识别概率
        prob_idx = prob[0, cls_idx]

        return  cls_idx.cpu().detach().item(), prob_idx.cpu().detach().item()


    def recognize_by_file(self, imgfile):
        img = cv2.imread(imgfile)
        return self.recognize(img)

if __name__ == "__main__":
    reco = Recognizer()
    idx, prob = reco.recognize_by_file("imgs/img_9_9.png")
    print(F"识别结果：{idx}，概率：{prob}")