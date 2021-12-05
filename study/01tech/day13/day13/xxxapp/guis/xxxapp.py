from PyQt5.QtWidgets import QApplication
import sys
from xxxapp.guis.login.xxxlogin import XXXLogin
from xxxapp.guis.home.xxxhome import XXXHome 

class XXXApp(QApplication):
    def __init__(self):
        super(XXXApp, self).__init__(sys.argv)
        self.login = XXXLogin()
        self.home = XXXHome()
        # self.home.hide()  # 对话框默认隐藏
        self.login.signal_home.connect(self.recv_login_info)
        self.login.show()
        # self.home.show()  # 一定等登录成功才显示

    def recv_login_info(self):
        # print("登录成功，启动系统的主界面")
        self.home.show()
        self.login.destroy()