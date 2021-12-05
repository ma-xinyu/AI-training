from PyQt5.QtWidgets import QDialog,QPushButton,QLabel,QLineEdit

class LDialog(QDialog):

    def __init__(self):
        super(LDialog,self).__init__()
        #窗口设置
        self.resize(600, 400)
        self.move(240,200)
        #窗口起名
        self.setWindowTitle("登陆窗口")

        #label      QLabel
        self.lab = QLabel("<font color=red><h1><b>登陆界面</h1></b></font>",self)
        #self.lab.resize(10,10)
        self.lab.move(240,80)
        #登陆按钮   QPushButton
        self.btn1 = QPushButton("登录",self)
        self.btn1.resize(100,30)
        self.btn1.move(100,250)
        #退出按钮   QPushButton
        self.btn2 = QPushButton("退出",self)
        self.btn2.resize(100,30)
        self.btn2.move(400,250)
        #输入行     QLineEdit
        self.lab1 = QLabel("<h3>账号:</h3>",self)
        self.lab1.move(180,140)
        self.edit1 = QLineEdit("",self)
        self.edit1.move(240,140)
        self.edit1.setPlaceholderText("请输入账号")
        self.lab2 = QLabel("<h3>密码:</h3>",self)
        self.lab2.move(180,180)
        self.edit2 = QLineEdit("",self)
        self.edit2.move(240,180)
        self.edit2.setPlaceholderText("请输入密码")

        #信号和槽
        self.btn1.clicked.connect(self.clicked_log)
        #self.btn1.clicked.connect(self.clicked_log_end)
        self.btn2.clicked.connect(self.clicked_logout)

    def clicked_logout(self,e):
        print("退出登陆界面")
        self.close()

    def clicked_log(self,e):
        print("点击了登录")

    def clicked_log_end(self,e):
        self.close()
