from PyQt5.QtWidgets import QApplication
from uis.wdialog import WDialog
import sys

class WApplication(QApplication):

    def __init__(self):
        super(WApplication, self).__init__(sys.argv)
        # 添加自己的数据
        self.dlg = WDialog()
        self.dlg.show()
    
    # 添加自己的计算