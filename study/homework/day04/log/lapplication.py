from PyQt5.QtWidgets import QApplication
from log.ldialog import LDialog#让对话框成为应用的成员
import sys

class LApplication(QApplication):

    def __init__(self):
        super(LApplication,self).__init__(sys.argv) #套路

        #添加自己的数据
        #窗口
        self.dlg = LDialog()
        self.dlg.show()

#添加自己的计算