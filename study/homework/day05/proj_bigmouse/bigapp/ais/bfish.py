from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtGui import QPen,QColor
import random


class BFish(QThread):
    signal_open = pyqtSignal()

    def __init__(self):
        super(BFish,self).__init__()
        self.list = [0,90,180,270]
        self.x = 100
        self.y = 100
        self.s = 200    #大小
        self.d = random.choice(self.list)      #0R 90U 180L 270D
        self.m = 30     #角度

        self.x1 = 0
        self.y1 = 0
        self.s1 = 0
        self.d1 = 0
        self.m1 = 0
        self.x2 = 0
        self.y2 = 0
        self.s2 = 0
        self.d2 = 0
        self.m2 = 0

        self.c1 = random.randint(0,255)
        self.c2 = random.randint(0,255)
        self.c3 = random.randint(0,255)

        self.is_open = False

    def swim(self):
        if self.d == 0:
            self.x += 5
        if self.d == 90:
            self.y -= 5
        if self.d == 180:
            self.x -= 5
        if self.d == 270:  
            self.y += 5


    def change_dir(self,d): #改变方向
        self.d = d

    def open_mouth(self):
        if self.is_open:
            self.m += 5
            if self.m >= 30:
                self.is_open = not self.is_open
                self.m = 30
                
        else:
            self.m -= 5
            if self.m <= 0:
                self.is_open = not self.is_open
                self.m = 0

    def change_d(self):
        if self.d == 0 and self.x + self.s >= 800:
            self.change_dir(random.choice(self.list))
        elif self.d == 180 and self.x <= 0:
            self.change_dir(random.choice(self.list))
        elif self.d == 90 and self.y <= 0:
            self.change_dir(random.choice(self.list))
        elif self.d == 270 and self.y + self.s >= 600:
            self.change_dir(random.choice(self.list))
        else:
            pass
            

    def show_me(self,g):    #g = QPrinter
        #QPen
        color = QColor(self.c1,self.c2,self.c3)
        pen = QPen(color,4.0,Qt.DashDotLine,Qt.RoundCap,Qt.RoundJoin)
        #颜色 粗细 笔的样式 ...
        g.setPen(pen)   #QPrinter和pen绑在一起

        if self.d == 0:
            self.s1 = self.s /10    #eyes
            self.x1 = self.x + self.s / 2
            self.y1 = self.y + self.s / 4
            self.d1 = self.d
            self.m1 = 0

            self.s2 = self.s    #tail
            self.x2 = self.x - self.s / 2
            self.y2 = self.y
            self.d2 = self.d
            self.m2 = 120

        elif self.d == 90:
            self.s1 = self.s /10    #eyes
            self.x1 = self.x + self.s * 3 / 4
            self.y1 = self.y + self.s / 4
            self.d1 = self.d
            self.m1 = 0

            self.s2 = self.s    #tail
            self.x2 = self.x 
            self.y2 = self.y + self.s / 2
            self.d2 = self.d
            self.m2 = 120

        elif self.d == 180:
            self.s1 = self.s /10    #eyes
            self.x1 = self.x + self.s / 2
            self.y1 = self.y + self.s / 4
            self.d1 = 180
            self.m1 = 0

            self.s2 = self.s    #tail
            self.x2 = self.x + self.s / 2
            self.y2 = self.y
            self.d2 = self.d
            self.m2 = 120

        elif self.d == 270:
            self.s1 = self.s /10    #eyes
            self.x1 = self.x + self.s * 3 / 4
            self.y1 = self.y + self.s / 4
            self.d1 = self.d
            self.m1 = 0

            self.s2 = self.s    #tail
            self.x2 = self.x 
            self.y2 = self.y - self.s / 2
            self.d2 = self.d
            self.m2 = 120

        g.drawPie(
                self.x,self.y,
                self.s,self.s,
                (self.d + self.m) * 16,
                (360 - 2 * self.m) * 16,             
        )
        g.drawPie(
                self.x1,self.y1,
                self.s1,self.s1,
                (self.d1 + self.m1) * 16,
                (360 - 2 * self.m1) * 16,    
        )
        g.drawPie(
                self.x2,self.y2,
                self.s2,self.s2,
                (self.d2 + self.m2) * 16,
                (360 - 2 * self.m2) * 16,
        )


    def run(self):
        #run结束线程就死亡
        while True:
            self.open_mouth()       #让鱼不停地进行张嘴的动作
            self.swim()
            self.change_d()
            self.signal_open.emit() #信号发送
            QThread.usleep(100000)  #wait 1000 000 是一秒