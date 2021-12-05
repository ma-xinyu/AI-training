from PyQt5.QtWidgets import QDialog
from xxxapp.guis.login.loginui import Ui_Login
from xxxapp.devs.login.facedev import FaceThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, Qt

"""
https://doc.qt.io/qt-5/stylesheet-reference.html
"""
class XXXLogin(QDialog):
    signal_home = pyqtSignal()
    def __init__(self):
        super(XXXLogin, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)
        # 视频采集任务线程
        self.face_th = FaceThread()
        self.face_th.signal_face.connect(self.show_login_video)
        self.face_th.start()

    def show_login_video(self, h, w, c, data, login_ok):
        if login_ok:
            # 关闭登录窗口
            self.close()
            # 显示主窗体
            self.signal_home.emit()
        else:
            # 显示图像
            qimg = QImage(data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.ui_login.lbl_face_video.setPixmap(pixmap)
            self.ui_login.lbl_face_video.setScaledContents(True) 
            
    
    def closeEvent(self, e):
        self.face_th.close()
