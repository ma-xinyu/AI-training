from PyQt5.QtWidgets import QDialog

from garbageapp.guis.garbage.garbageui import Ui_garbage
from garbageapp.devs.garbage.garbagedev import GarbageThread
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
from garbage_yolov4.garbagedet import GarbageDetector
from garbageapp.biz.garbage.names import GarbageDAO

"""
    Date:
    Function:
    Author:
    Comment:
    模块注释
        xxxxxxxxxxx
"""

class GarbageHome(QDialog):
    def __init__(self):
        super(GarbageHome, self).__init__()
        self.ui_garbage = Ui_garbage()
        # self.garbage_recognizer = GarbageRecognizer()
        self.pixmap = QPixmap()
        self.ui_garbage.setupUi(self)
        self.ui_garbage.CatchButton.clicked.connect(self.show_garbage_picture)
        self.ui_garbage.RecogButton.clicked.connect(self.show_result)
        self.garbage_detector = GarbageDetector()
        self.garbage_names = []
        # self.counter = 0
        self.dao = GarbageDAO()

    
    def init_dev(self):
        self.garbage_th = GarbageThread()
        self.garbage_th.signal_garbage.connect(self.show_garbage_video)
        
        # self.ui.garbage.RecogButton.clicked.connect(self.garbage_recognizer.recognzie(QPixmap.toImage(self.pixmap)))
        self.garbage_th.start()

    def show_garbage_video(self, h, w, c, data):
        self.h = h
        self.w = w
        self.c = c
        self.data = data
        qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qimg)
        self.ui_garbage.VideoWidget.setPixmap(self.pixmap)
        self.ui_garbage.VideoWidget.setScaledContents(True)
    
    def show_garbage_picture(self):
        self.h_s = self.h
        self.w_s = self.w
        self.c_s = self.c
        self.data_s = self.data
        self.ui_garbage.PictureWidget.setPixmap(self.pixmap)
        self.ui_garbage.PictureWidget.setScaledContents(True)
        # self.show_result()

    def show_result(self):
        self.frame = np.frombuffer(self.data_s,dtype=np.uint8).reshape(self.h_s,self.w_s,self.c_s)
        # print(self.frame)
        pred = self.garbage_detector.detect(self.frame)
        if pred is not None:
            # 循环处理识别结果
            for x1, y1, x2, y2, p, cls_id in pred:
                # 概率过滤
                if p > 0.1:
                    cls_id = int(cls_id)
                    name = self.garbage_detector.get_name(cls_id)
                    self.garbage_names.append(name)
                    # self.counter += 1
        recog_ok = False
        if self.garbage_names != []:
            most_name = max(self.garbage_names, key=self.garbage_names.count)
            recog_ok = self.dao.validate(most_name)
            self.garbage_names = []
        if recog_ok:
            self.ui_garbage.ResultWidget.setText(most_name)
        else:
            self.ui_garbage.ResultWidget.setText("没有识别到垃圾")


    
    def closeEvent(self, e):
        #关断线程
        self.garbage_th.close()


