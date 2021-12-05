from PyQt5.QtCore import QThread, pyqtSignal
import cv2


class BVideoTh(QThread):

    signal_video = pyqtSignal(int, int, int, bytes)
    
    def __init__(self):
        super(BVideoTh, self).__init__()
        # 创建摄像头对象
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    
    def run(self):
        while True:
            status, frame = self.dev.read()
            if status:
                h, w, c = frame.shape
                # 做一个图像处理
                # frame[100:200,:,0] = 0
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 图像的特征处理
                # frame = cv2.GaussianBlur(frame, ksize=(11, 11), sigmaX=5)
                frame = cv2.Sobel(frame, ddepth=-1, dx=2, dy=2, ksize=5, delta=80)
                self.signal_video.emit(h, w, c, frame.tobytes())
            else:
                print("设备故障！")
                break  # 结束线程
            QThread.usleep(100000)
    