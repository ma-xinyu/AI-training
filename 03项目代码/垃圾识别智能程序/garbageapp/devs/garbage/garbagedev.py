from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from garbage_yolov4.garbagedet import GarbageDetector

class GarbageThread(QThread):
    signal_garbage = pyqtSignal(int, int, int, bytes)
    
    
    def __init__(self):
        super(GarbageThread, self).__init__()
        # 创建设备
        self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.is_ok = False
        self.detector = GarbageDetector()


    def run(self):
        while not self.is_ok:
            # 采集视频
            status, frame = self.dev.read()
        
            if not status: 
                self.is_ok = True
                continue
            pred = self.detector.detect(frame)

            if pred is not None:
                # 循环处理识别结果
                for x1, y1, x2, y2, p, cls_id in pred:
                    # 概率过滤
                    if p > 0.1:
                        cls_id = int(cls_id)
                        name = self.detector.get_name(cls_id)
                        
                        # 实现标注
                        x1 = int(x1)
                        y1 = int(y1)
                        x2 = int(x2)
                        y2 = int(y2)
                        # 线条等自定义显示
                        cv2.rectangle(frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=4)
                        cv2.putText(
                            frame, 
                            F"{name}:{p:.2f}", 
                            org=(x1, y1 - 50 ), 
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.5,
                            color=(0, 255, 255),
                            thickness=1)
            
            # 发送信号
            h, w, c = frame.shape

            frame = frame[:,:,::-1]
            self.signal_garbage.emit(h, w, c, frame.tobytes())
            QThread.usleep(50000)


    def close(self):
        self.is_ok=True
        # 结束线程-暴力型
        self.terminate()
        #while isRunning():
            #pass
        # 释放设备
        self.dev.release()