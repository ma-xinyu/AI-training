from PyQt5.QtWidgets import QDialog
from bigapp.uis.videoui import Ui_Video
from bigapp.uis.bvideo import BVideoTh
from PyQt5.QtGui import QImage,QPixmap

class BDialog(QDialog):
    def __init__(self):
        super(BDialog, self).__init__()
        self.ui = Ui_Video()
        self.ui.setupUi(self)

        #启动摄像任务 创建BVideoTh的对象
        self.th = BVideoTh()
        #绑定信号和槽
        self.th.signal_video.connect(self.show_video)
        self.th.start()


    def show_video(self , h , w , c , data):
        #print("有图像发送")
        #构造Qt图像 QImage
        qimg = QImage(data , w , h , w * c , QImage.Format_RGB888)  #w.c是字节数 宽*通道数

        #转换成QPixmap才能显示
        qpixmap = QPixmap.fromImage(qimg)

        #设置到标签
        self.ui.lab_video.setPixmap(qpixmap)
        #设置视频缩放来适应标签大小
        self.ui.lab_video.setScaledContents(True)

