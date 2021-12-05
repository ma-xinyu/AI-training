from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import Qt

class  WDialog(QDialog):


    def __init__(self):
        super(WDialog, self).__init__()
        self.btn = QPushButton("打开", self)
        
        self.btn.resize(100,30)
        self.btn.move(100,100)

        self.resize(600, 400)
        self.move(200,200)

        self.setWindowTitle("视频监控")

        # 信号与槽函数绑定一起
        self.btn.clicked.connect(self.handle_clicked)
    
    def closeEvent(self, e):
        print("窗体关闭，释放资源")

    def keyPressEvent(self, e):
        # print("按键:",e.key(), ",", e.text(), e.modifiers())
        if e.modifiers() == Qt.ControlModifier and  e.key() == Qt.Key_D:
            print("Ctrl+ D")
    
    def keyReleaseEvent(self, e):
        print("释放键")

    # 确定信号 clicked()
    # 槽函数的名字可以不一样，但是参数必须完全一样
    def handle_clicked(self):
        print("按钮点击")


    