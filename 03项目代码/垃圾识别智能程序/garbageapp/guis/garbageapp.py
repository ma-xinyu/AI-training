from PyQt5.QtWidgets import QApplication
import sys
from garbageapp.guis.login.garbagelogin import GarbageLogin
from garbageapp.guis.garbage.garbagehome import GarbageHome 


class GarbageApp(QApplication):
    def __init__(self):
        super(GarbageApp, self).__init__(sys.argv)
        self.login = GarbageLogin() #登录对话框
        self.home = GarbageHome()   #主对话框
        # self.home.hide()  # 主对话框默认隐藏
        
        self.login.signal_home.connect(self.recv_login_info)
        self.login.show()   # 登录对话框一直显示，直到成功登录
        # self.home.show()  # 主界面一定等登录成功才显示

    def recv_login_info(self):
        # print("登录成功，启动系统的主界面")
        self.login.destroy()
        self.home.init_dev()
        self.home.show()
        