from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPainter
from bigapp.ais.bfish import BFish
from PyQt5.QtCore import Qt

class BDialog(QDialog):
    def __init__(self):
        super(BDialog, self).__init__()
        self.setWindowTitle("大嘴鱼")
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        
        self.fish = BFish()
        self.fish.signal_open.connect(self.repaint)
        self.fish.start()

        self.fish2 = BFish()
        self.fish2.x = 300
        self.fish2.y = 300
        self.fish2.s = 80
        self.fish2.signal_open.connect(self.repaint)
        self.fish2.start()
    
    def keyPressEvent(self, e):
        # 键盘的按键处理 ↑ ↓ ← →
        key = e.key()
        if key == Qt.Key_Right:
            self.fish2.change_dir(0)
            self.fish2.swim()
        if key == Qt.Key_Up:
            self.fish2.change_dir(90)
            self.fish2.swim()
        if key == Qt.Key_Left:
            self.fish2.change_dir(180)
            self.fish2.swim()
        if key == Qt.Key_Down:
            self.fish2.change_dir(270)
            self.fish2.swim()
        
    def paintEvent(self, e):
        # 完成绘制工作
        # 构建绘制器
        painter = QPainter(self)
        # 绘制
        # painter.drawPie(100,100, 200, 200, 45 * 16, (360 - 2 * 45) * 16)
        self.fish.show_me(painter)
        self.fish2.show_me(painter)
