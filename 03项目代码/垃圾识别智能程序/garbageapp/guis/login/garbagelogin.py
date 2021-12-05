from PyQt5.QtWidgets import QDialog
from garbageapp.guis.login.loginui import Ui_Login
from garbageapp.devs.login.facedev import FaceThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5 import QtGui
import time
import cv2

"""
https://doc.qt.io/qt-5/stylesheet-reference.html
"""
class GarbageLogin(QDialog):
    signal_home = pyqtSignal()
    def __init__(self):
        super(GarbageLogin, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)
        # 视频采集任务线程
        self.face_th = FaceThread()
        self.face_th.signal_face.connect(self.show_login_video)
        self.face_th.start()
        self.face_th.signal_picture.connect(self.change_picture)

    def show_login_video(self, h, w, c, data, login_ok):
        if login_ok:
            # 关闭登录窗口
            """image_src = cv2.imread("garbageapp/guis/login/222.jpg")
            h, w, c =image_src.shape
            image = QImage(image_src.tobytes(),w,h,c*w,QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.ui_login.label.setPixmap(pixmap)
            self.ui_login.label.setScaledContents(True)"""
            
            # self.ui_login.label.setPixmap(QtGui.QPixmap("garbageapp/guis/login/222.jpg"))
            # time.sleep(20)
            
            self.close()
            # 显示主窗体，发出信号
            self.signal_home.emit()
        else:
            # 显示图像
            # self.ui_login.label.setPixmap(QtGui.QPixmap("garbageapp/guis/login/222.jpg"))

            qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.ui_login.lbl_face_video.setPixmap(pixmap)
            self.ui_login.lbl_face_video.setScaledContents(True)    #缩放适应窗体
            
            """time.sleep(1)
            image_src = cv2.imread("garbageapp/guis/login/222.jpg")
            h, w, c =image_src.shape
            image = QImage(image_src.tobytes(),w,h,c*w,QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(image)
            self.ui_login.label_2.setPixmap(pixmap)
            self.ui_login.label_2.setScaledContents(True)"""
            
    def change_picture(self):
        self.ui_login.label.setPixmap(QtGui.QPixmap("garbageapp/guis/login/22.jpg"))
        self.ui_login.label_2.setPixmap(QtGui.QPixmap("garbageapp/guis/login/33.jpg"))

    
    def closeEvent(self, e):
        #关断线程
        self.face_th.close()
