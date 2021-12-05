# 引入模块
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel
import sys

app = QApplication([]) 
dlg = QDialog()
dlg.resize(600, 400)
dlg.move(100, 100)

btn = QPushButton("确定", dlg)
btn.resize(100, 30)
btn.move(100, 100)

lbl = QLabel("<font color=red><b><s>我是靓仔</s></b></font>", dlg)
lbl.resize(100, 100)
lbl.move(100, 200)

dlg.show()
status = app.exec()  
sys.exit(status) 
