# 引入模块
import PyQt5.QtWidgets
# import PyQt5.QtCore
# import PyQt5.QtGui
import sys

# 创建对象
"""
    PyQt5包路径
    QtWidgets是模块：不是Python，是C写的扩展名是pyd的dll模块
"""
app = PyQt5.QtWidgets.QApplication([])   # 传递命令行参数 = main的argv （argc， argv， arge）
# ========================
# 创建窗体，处理事件
dlg = PyQt5.QtWidgets.QDialog()
dlg.show()
# ========================
status = app.exec()  # 开始循环处理事件、信号等。

sys.exit(status)  # 可选：返回程序运行状态给操作系统
