from PyQt5.QtCore import QThread,pyqtSignal
import cv2

class BVideoTh(QThread):

    #高，宽，通道，字节码
    signal_video = pyqtSignal(int,int,int,bytes)

    def __init__(self):
        super(BVideoTh,self).__init__()
        #创建摄像头驱动
        self.dev = cv2.VideoCapture(0,cv2.CAP_DSHOW) #0 摄像头编号

    def run(self):
        while True:
            #返回状态、图像
            status,frame = self.dev.read()
            if status:
                #print(frame.shape)
                h , w , c = frame.shape     #高，宽，通道
                #做图像处理
                #frame[:,:,2] = 0   #去蓝
                #frame[ : , : : 3] = 255 #列 每三个像素变白一个
                frame[frame[:,:,0]>100] = 255 #像素中通道1分量大于100，就变白
                #通道颜色交换
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                self.signal_video.emit(h,w,c,frame.tobytes())   #frame.tobytes()转换为字节数组
            else:
                print("设备故障！")
                break   #结束线程
            QThread.usleep(100000)