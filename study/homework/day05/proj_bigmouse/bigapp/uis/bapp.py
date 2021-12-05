from PyQt5.QtWidgets import QApplication
from bigapp.uis.bdialog import BDialog
import sys

class BApp(QApplication):

    def __init__(self):
        super(BApp,self).__init__(sys.argv)
        #构建QApplication与QDialog的关系（类与类）：包含
        self.dlg = BDialog()
        self.dlg.show()