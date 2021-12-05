from yolov4.models import Darknet    # YOLOv4网络结构的实现
from yolov4.utils.datasets import *  # 引入所有数据集处理函数
from yolov4.utils.utils import *     # 引入yolo的计算函数：比如iou计算

import torch     # pytorch的包
import os        # 数据文件的管理：.pt, .cfg, .names
import numpy


class FaceDetector:

    def __init__(self):
        super(FaceDetector ,self).__init__()
        # 条件1：文件准备
        current_dir = os.path.dirname(__file__)
        self.cfg_file = os.path.join(current_dir, "data/yolov4-tiny.cfg")
        self.mod_file = os.path.join(current_dir, "data/faces.pt")
        self.names_file = os.path.join(current_dir, "data/faces.names")

        self.img_size = 640   # 设置预测的图像大小
        # 条件2：网络结构
        self.net = Darknet(cfg=self.cfg_file, img_size=self.img_size)
        # 条件3：加载模型
        state_dict = torch.load(self.mod_file)["model"]
        self.net.load_state_dict(state_dict) 
        # 条件4：GPU操作
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.net = self.net.cuda()
        # 条件5：加载names文件
        self.names = load_classes(self.names_file)
        print(self.names)
        # 条件6
        self.net.eval()   # train(开启)/eval(关闭): BatchNorm / Dropout

    def detect(self, img):
        """
            img：是ndarray数组图像
        """
        self.src_shape = img.shape 
        # 1. 图像格式预处理
        img = self.pre_image(img)
        # 2. 完成侦测
        return self.yolov4_det(img)
    
    def pre_image(self, img):
        # 图像的预处理
        # 1. 按照self.img_size缩小图像
        # print(img.shape)
        img = letterbox(img, new_shape=self.img_size)[0]
        # print(img.shape)
        # 2. 颜色通道进行转换[HWC]->[CHW]，并且BGR->RGB
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) : BGR->RGB
        # img = img[:,:, ::-1]  # BGR -> RGB
        # img = img.transpose(2, 0, 1)
        img = img[:,:, ::-1].transpose(2, 0, 1)
        # print(img.shape)
        # 3. 数组转换为连续空间（可选）
        img = numpy.ascontiguousarray(img)
        # 4. 转换为Tensor
        img = torch.from_numpy(img)
        # 5. 转换为FloatTensor
        img = img.float()
        # 6. 图像归一化
        img /= 255.0
        # 7. 确认图像是[NCHW]的四维图像
        if img.ndimension() == 3:
            img = img.unsqueeze(0)   # 扩展一个维度
            # print(img.shape)
        return img

    def yolov4_det(self, img):
        # 侦测过程
        # 1. GPU
        if self.CUDA:
            img = img.cuda()
        # 2. 预测
        pred = self.net(img)[0]   # 返回的元组第一个是预测结果，第二个是cfg的其他参数
        """
            pred[0] : 预测的所有目标
            pred[1] : 存放模型的数据
        """
        # print(type(pred), len(pred))
        # print(pred.shape)
        # torch.Size([1,            4800,               9])
        #            图像的编号      侦测的目标个数     5（id, cx, cy, w, h） + 4(p1, p2, p3, p4)
        # 3. 去重(非最大化抑制)
        pred = non_max_suppression(pred, 0.3, 0.2, merge=False, classes=None, agnostic=False)
        # 符合率0.3保留，重合率0.2去掉，merge重叠的不合并
        # print(pred)
        """
          返回：x1, y1, x2, y2, p, id
        """
        # 4. 放大还原   
        for det in pred:   # 循环所有图像中的目标
            if det is not None and len(det):  # 一张图像中的所有目标
                det[:, 0:4] = scale_coords(
                    img.shape[2:],             # 缩小后的图像大小
                    det[:, 0:4],              # 预测的目标的坐标
                    self.src_shape             # 原始图像大小
                ).round()  # 四舍五入
        if pred[0] is not None:
            return pred[0].cpu().detach().numpy()
        else:
            return None

    def get_name(self, cls_id):
        return self.names[cls_id]

    def detect_mark(self, img):
        """
            返回标注的图像
        """

        pred = self.detect(img)
        # 标注
        if pred[0] is not None:
            for x1, y1, x2, y2, p, cls_id in pred:
               # 类型转换
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                cls_id = int(cls_id)
                name = self.get_name(cls_id)
                cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(255, 255, 0), thickness=4)
                cv2.putText(
                    img, 
                    name, 
                    org=(x1, y1 - 50 ), #高一点
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=2.0,
                    color=(0, 0, 255),
                    thickness=3
                )
            return img
        else:
            return None
