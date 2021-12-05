from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPen, QColor

class BFish(QThread):
    signal_open = pyqtSignal()

    def __init__(self):
        super(BFish, self).__init__()
        self.x = 100
        self.y = 100
        self.s = 200
        self.d = 0  # 0R 90U 180L 270D
        self.m = 45
        self.is_open = False
    
    def swim(self):
        if self.d == 0:
            self.x += 1
        if self.d == 90:
            self.y -= 1
        if self.d == 180:
            self.x -= 1
        if self.d == 270:
            self.y += 1

    def change_dir(self, d):
        self.d = d
    
    def open_mouth(self):
        if self.is_open:
            self.m += 5
            if self.m >=45:
                self.is_open = not self.is_open
                self.m = 45
        else:
            self.m -= 5
            if self.m <= 0:
                self.is_open = not self.is_open
                self.m = 0
    def show_me(self, g):
        # QPen
        color = QColor(255, 0, 0)
        pen = QPen(color, 4.0, Qt.DashDotLine, Qt.RoundCap, Qt.RoundJoin)
        g.setPen(pen)
        g.drawPie(
            self.x, self.y, 
            self.s, self.s, 
            (self.m + self.d)* 16, 
            (360 - 2 * self.m) * 16
        )


    def run(self):
        # run结束线程死亡
        while True:
            self.open_mouth()
            self.signal_open.emit()
            QThread.usleep(100000)
