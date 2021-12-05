from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPainter
from bigapp.ais.bfish import BFish
from PyQt5.QtCore import Qt

class  BDialog(QDialog):

    def __init__(self):
        super(BDialog,self).__init__()
        self.setWindowTitle("大嘴鱼")
        self.setFixedSize(800,600)
        #self.setWindowFlags(Qt.CustomizeWindowHint) #自定义窗口
        self.fish = BFish()
        self.fish.signal_open.connect(self.repaint) #刷新
        self.fish.start()
        #启动线程

        self.fish2 = BFish()
        self.fish2.x = 300
        self.fish2.y = 300
        self.fish2.s = 80
        self.fish2.signal_open.connect(self.repaint)
        self.fish2.start()

        self.fish3 = BFish()
        self.fish3.x = 500
        self.fish3.y = 400
        self.fish3.s = 50
        self.fish3.signal_open.connect(self.repaint)
        self.fish3.start()

    def keyPressEvent(self,e):
        self.fish.swim()

    def keyPressEvent(self,e):
        #print("dd")
        #键盘的上下左右
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

    def paintEvent(self,e):
        #print("窗体在绘制")
        #构建绘制器
        painter = QPainter(self)#self是画布
        #绘制
        #painter.drawPie(100,100,200,200,45*16,(360-2*30)*16)
        self.fish.show_me(painter)
        self.fish2.show_me(painter)
        self.fish3.show_me(painter)