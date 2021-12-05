# 人工智能实训技术博文（1）
## 本篇技术博文记录实训第1周~第3周主要知识点
> 前三周的课程集中在非项目工程的基础编程知识与工具的讲解、使用，主要集中在：
>> 1.python工程与语法
      2.Qt编程
      3.git的使用
### 一、python工程与python语法
   1.在vs code中终端运行的两种表示
		格式：python -m 包路径.包路径.模块   （模块就是python文件名）
		python -m py文件名（无后缀）
		python py文件（加后缀）

		在VSCodde中设置选择shell的类型bat（command prompt shell）

		养成保存的习惯，保存之后才能运行出来
	
   2.python >> help(名) 获取在线帮助
		dir(对象)查看这个对象的成员
		 
		例：print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
		
		参数：objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
			sep -- 用来间隔多个对象，默认值是一个空格。
			end -- 用来设定以什么结尾。默认值是换行符\n，我们可以换成其他字符串。
			file -- 要写入的文件对象。
			flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
			input(prompt=None, /)
			参数：prompt:--提示信息

   3.python提供产生列表的方法：range
		range(start, stop[, step])
		参数：start:  计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
		stop:  计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
		step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

   4.写好的.py文件打包添加到.bat文件使用：    
		例：@python -m list 	（list是.py文件）
		bat文件是dos下的批处理文件。批处理文件是无格式的文本文件，它包含一条或多条命令。
		它的文件扩展名为 .bat 或 .cmd。
		在命令提示下输入批处理文件的名称，或者双击该批处理文件，系统就会调用cmd.exe按照该文件中各个命令出现的顺序来逐个运行它们。

   5.random
		import random
		print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
		print( random.random() )             # 产生 0 到 1 之间的随机浮点数
		print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
		print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
		print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
		print random.sample('zyxwvutsrqponmlkjihgfedcba',5)	# 多个字符中生成指定数量的随机字符
		print random.choice(['剪刀', '石头', '布'])		# 随机选取字符串
		items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		print random.shuffle(items)			# 打乱排序

### 二、Qt编程的基本介绍
   1. 安装第三方模块
	pip install PyQt5
	技巧：
		1.在百度输入 pip 模块名，就能获取安装帮助
		2. pip list 查看所有安装的模块
		3. pip list  | find "查找的关键字"
		4.dir *.pyd 动态库文件

   2. 使用类
		创建对象
		调用对象的成员函数完成数据处理
	
   3. Qt应用编程模式	
		1.创建QApplication （管理应用程序）
		2.创建窗体与组件
		3.Application阻塞监控事件

		---补充
		QtWidgets ： Qt GUI所有的类
		QtCore ： 负责系统层面的封装：QThread：线程
		QtGui： 负责底层的图形绘制
		使用动态库
			与python的模块完全一样
		---补充
		import与from的使用
		方式一：
			import PyQt5.QtWidgets
				PyQt5.QtWidgets.QAppliction
		方式二：
			from PyQt5.QtWidgets import QApplication, QDialog
				QApplication

   4. 继承使用（override）
		： 复用
		： 创新：overide， 添加新的过程

   5. 项目的结构
		cd "路径"；tree /F
		包路径建议放一个__init__.py
	
	帮助文档：
		https://doc.qt.io/qt-5/classes.html

### 三、Qt编程的基本思路
   1.基本模板
		#引入模块
		import PyQt5.QtWidgets
		import PyQt5.QtCore
		import PyQt5.QtGui
		import sys

		#创建对象
		app = PyQt5.QtWidgets.QApplication([])   #传递命令行参数 = main的argv(argc,argv,arge)

		#创建窗体
		dlg = PyQt5.QtWidgets.QDialog()
		dlg.show()

		status = app.exec() #开始循环处理事件、信号等
		sys.exit(status)

   2.简单的按钮、标签
		dlg = QDialog()
		btn = QPushButton("ok",dlg)	#按钮
		lbl = QLabel

   3.继承
		ex03、wapplication、wdialog 展示了继承；模板都一样

		编程模式：
			继承QApplication         -------|
				|- 继承窗体QDialog   --------| -
					类与类的关系： 依赖关系： 聚合关系 ： 包含关系

		在wapplication种加入from uis.wdialog import WDialog(有组织结构)：
		将继承的wdialog加到应用层,让对话框成为应用的成员，应用层管理窗口，窗口管理按钮 good!

   4.在dialog.py中，self表示窗口的性质，self.btn表示按钮的属性

   5.#信号与槽函数绑定一起
        	self.btn.clicked.connect(self.handle_clicked):
				handle_clicked(self) 是槽函数
				btn.clicked 	是事件


## 四、git的使用
   1.场景一：（每个项目只做一次）
	第一次创建仓库初始化，提交master公共文件
	README.md
	其他文件
	01. 创建工作目录
		并且使用cd切换到工作路径   cd \
	02. 初始化为本地仓库
		git init
	03. 第一次使用需要设置个人的名字与邮件
		git config --global user.name "yangqiang"
		git config --global user.email "38395870@11.com"
	--------------------------------
	04. 编码工作 + README.md
		- README.md建议创建
	05. 添加代码到仓库
		git add  *
	06. 设置提交的信息
		git commit -m 第一从更新 -a
	07. 提交前设置服务器参数
		- 设置本地代理名
		查看：git remote -v
		设置：git remote add ma http://  yangqiang:yang123(账号：密码)  @39.98.127.39:3000/yangqiang/Test2019.git(仓库的链接)
	08. 物理更新服务器代码
		git push --set-upstream ma master (master分支名，服务器默认的分支是master)
	
   2.场景二：提交作业（每天都做，做自己分支的任务）
		01. 创建工作目录
			cd \;	cd wk2019\
		02. 初始化仓库
			git init
			----------------准备工作
		03. 建立服务器代理
			git remote add origin http://yangqiang:yang123@39.98.127.39:3000/yangqiang/Test2019.git

			--删除
			git remote remove  代理名

		04. 拉取代码
			git pull --rebase origin master    # master是主分支名，也可以直接拉取某个分支

		----------------拉取代码
		05. 查看分支
			git branch

		06. 创建分支
			git branch 分支名

		07. 切换分支
			git checkout 分支名

		08. 开始开发，产生目录与代码
			加了新的会有 U 提示
		09. 添加新的文件到仓库
			git add *
		10. 设置提交的消息
			git commit -m  更新了GUI  -a

		11. 提交
			git push --set-upstream origin louis

   3.场景三：（项目中可能做两三次，组长汇总代码，组员再从主分支拉取，再加自己update的内容）
	最终或者阶段成果代码的分支合并；

		01. 创建工作目录（建一个用于汇总的目录）

		02. 克隆服务器仓库
			git clone http://yangqiang:yang123@39.98.127.39:3000/yangqiang/Test2019

		03. 拉取需要合并的分支（同时切换本地分支）
			git checkout -b louis（本地建立的分支）  origin/louis（从git拉取的子分支）

		04. 合并分支
			- 注意：确保在master分支进行合并：把分支合并到master
			git merge louis

		05. 提交主分支到仓库
			. 添加代码带仓库
				git add  *
			. 设置提交信息
				git commit -m 第一阶段合并 -a
			. 物理更新文件
				git push --set-upstream origin master 

# 人工智能实训技术博文（2）
## 本篇技术博文记录实训第4周~第5周知识点及工程概要
> 后两周课程着重讲解最终的项目实现，并对人工智能的机器学习、图像识别进行了入门讲解，主要内容包含：
>> 1.opencv的使用与图像处理
>> 2.ui设计与多线程的实现
>> 3.卷积特征的学习原理
>> 4.项目文件的结构与搭建
### 一、图像处理
   1. opencv：
		core：图像的基本表示
		imgproc：图像处理
		imgcodecs：图像解码：图像IO
		videoio：摄像头与视频的IO
   2. 图像的加载与保存
		retval=cv.imread(filename[, flags]) 	
		例子：img = cv2.imread("import.png",cv2.IMREAD_COLOR)
		返回类型：numpy.ndarray

   3. 图像格式
		numpy.ndarray
			|- 数组
			|- 彩色图像是3维数组：(720, 1280, 3) == (height，width，channel/depth)
			|- 深度在opencv：通道 + 通道的基本类型 
			0xFF 00 00 : BGR 而在Qt中使用 RGB888
		构造ndarray就是构造一个图像（不方便）
		【构造数组（通道数只能是1，3，4）】

   4. 使用python的数据来构造ndarray
		补充：解析表达式：
			list = [5 for x in range(5)]
			print(list)
			>>[5, 5, 5, 5, 5]

   5. 图像的基本操作
		支持的图像：bmp/jpg/png/gif/tiff

   6. 下标运算：[]  ： 右：取值， 左：赋值
		1. 整数，整数数组
		2. 切片
			|- 对象表示
				slice(begin, end, step) : [begin, end)
				slice(end) : begin = 0 ,step = 0
			|- 表达式表示
				begin:end:step	begin:end		end:
			例子：
				#表达式方式
				#img[50:100 , 50:100:3 , 0] = 255 #0表示第一个通道
				#img[: , : , 0] = 0     #去蓝
				#img[img > 100] = 0     #全部位置的全部通道像素大于100的，改为0
				#img[img[: , : , 0] > 100] = 0   #全部位置的第一个通道（蓝色元素）大于100，就改为0

## 二、代码与UI结合
   1. UI设计：
		01. 使用qtdesigner设计ui
			x,y；windowTitle；QObject改为Video
			A. 拖拽组件
			B. 设置组件属性：位置大小，标签，以及其他，
			C. 设置组件的名字： Video / lbl_video，text内容
			D. *设置槽函数
			E. *设计信号与槽
		02. 把ui翻译成python
			工具：pyuic5 -o 输出的文件(py文件)   被翻译的ui文件
			#tool.bat
		03. import python模块
		04. 创建ui对象
			self.ui = Ui_Video()
		05. 使用ui对象
			self.ui.setupUi(self)


   2. 摄像头：
		1.多任务实现
			01. 继承QThread
			02. override run函数
			03. 创建摄像头对象
			04. run实现摄像头的视频采集
			05. 启动线程

		2，数据抓取
			self.dev = cv2.VideoCapture(0, cv2.CAP_DSHOW) 	#创建摄像头驱动
			status, frame = self.dev.read()		#抓取信息


   3. 代码和界面的结合：（摄像头功能和显示界面结合）
		使用信号传递图像：
			01. 定义信号（一直为True）	signal_video
			02. 发送信号（run(self)中）	self.signal_video.emit(h,w,c,frame.tobytes())
			03. 定义槽函数		def show_video(self , h , w , c , data)
			04. 绑定信号与槽
			（信号一直为True,一直运行槽函数show_video,一直在Qt界面输出QPixmap）

		在Qt中显示图像：
			Qt中显示图像就用QPixmap
			（QPixmap主要是用于绘图，针对屏幕显示而最佳化设计，QImage主要是为图像I/O、图片访问和像素修改而设计的。
			当图片小的情况下，直接用QPixmap进行加载，画图时无所谓，当图片大的时候如果直接用QPixmap进行加载，会占很大的内存，一般一张几十K的图片，用QPixmap加载进来会放大很多倍，
			所以一般图片大的情况下，用QImage进行加载，然后转乘QPixmap用户绘制）

		图像的处理：
			在bvideo.py的run(self)中进行图像处理

## 三、卷积特征学习
   1. jupyterlab的使用：
	（LaTex语法：https://www.jianshu.com/p/d26c0b3b71ea）
	（show math as -> tex commands）
		01.M键进行 makedown 和 code 的转换
		02. - $$h(x)= \int _{- \infty} ^{\infty} f(\tau) g(x - \tau) \mathrm{d} \tau$$
		\int = 积分；\infty = 无穷；\tau = 涛；、mathrm{d} = 罗马数字d
		03.![输出图片](dd.png)

   2. 离散的卷积公式的理解：（平滑运算 or 滤波运算）
		1.f(i,j)是3*3矩阵，g(x-i,y-j)是一个3*3模块，运算结果是周围的点加权变为一个新的像素点
		2.原图像是21*21，卷积核是3*3，那么新图像是19*19
		3.卷积运算就是在求梯度特征

		图像特征：
			像素的变化：
			Source Image -(Kernel) > Feature Map
			机器学习就是：找到一个Kernel，使我们得到的Feature Map更加容易识别（分类/侦测/分割/跟踪）
				- 多次卷积运算 -> 特征 -> 分类： 卷积神经网络 

   3. 卷积特征学习：（具体理解看代码中的自己加的注释）
		1.指针和数组：指针是程序员自己分配的，在栈区，数组是计算机分配的，在堆区
		2.几个常用的编程技巧（代码中看）
		3.张量（tensor）是多维数组，目的是把向量、矩阵推向更高的维度
			一阶张量可以理解为一个向量，二阶张量可以理解为矩阵，三阶张量可以理解成立方体，
			四阶张量可以理解成立方体组成的一个向量，五阶张量可以理解成立方体组成的矩阵，依次类推。

			图像通常具有三个维度：高度，宽度和颜色深度。虽然灰度图像（比如MNIST数字图像）只有一个颜色通道，因此可以保存在2D张量中，但按照惯例，图像张量始终是3D张量，灰度图像的彩色通道只有一维。
			因此，如果图像大小为256×256 ，那么128张灰度图像组成的批量可以保存在一个形状为（128，256，256，1）的张量中，而128张彩色图像组成的批量则可以保存在一个形状为（128，256，256，3）的张量中。
		4.求导（grad）：
		5.数据集：
			torch的图像格式：NCHW：数量 通道 高度 宽度（img：高 宽 通道）
			*255和/255：*255是张量变图像，/255则相反，
				为了保证精度，经过了运算的图像矩阵的数据类型会从unit8型变成double型。
				如果直接显示，我们会发现显示的是一个白色的图像。
				这是因为对double型是认为在0~1范围内，即大于1时都是显示为白色，而显示uint8型时是0~255范围
		6.lenet5模型：
			（矩阵）Conv2d : 卷积，根据卷积核进行 边-核+1 的图像处理
			max_pool2d : 磁化，降维，将图像进行 a x a 的缩小
			relu : 修正图像（激活函数），inplace : 在原矩阵上改变
			（矩阵）Linear : 全连接，把好多好多的像素特征点集合成几个特征，这些特征对应某个结果都有一个概率，概率最大的就是预测值

		    输出：
			当使用Softmax函数作为输出节点的激活函数的时候，一般使用交叉熵作为损失函数。
				dim(使 某一行 / 某一列 / 某个对应位置 和为1) : 
			argmax的结果是使得f(x)取得最大值的x点集。
				假设有一个函式 f(t)，t 的可能范围是 {0,1,2}，f(t=0) = 10 ; f(t=1) = 20 ; f(t=2) = 7，那分别对应的y如下：
				y = max f(t) = 20
				y= argmax f(t) = 1

   4. 分类器：
		该函数或模型能够把数据库中的数据纪录映射到给定类别中的某一个，从而可以应用于数据预测。
		总之，分类器是数据挖掘中对样本进行分类的方法的统称，包含决策树、逻辑回归、朴素贝叶斯、神经网络等算法。

		影响一个分类器错误率的因素
		　　(1)、训练集的记录数量。
		　　(2)、属性的数目。
		　　(3)、属性中的信息。
		　　(4)、待预测记录的分布。

		评估方法：
		有两种方法可以用于对分类器的错误率进行评估，它们都假定待预测记录和训练集取自同样的样本分布。
		　　(1) 保留方法(Holdout)
		　　(2) 交叉纠错方法(Cross validation)

			分类器中提到的概念：
			        线性回归
			        误差基本服从正态分布
			        逻辑分布代替正态分布，区别：逻辑分布有累积函数
			        最大似然函数：越大越好
			        损失函数：越小越好	交叉熵，梯度下降法
			步骤：
				加载数据集
				定义学习的w， b
				# 循环
				计算预测值
			 	使用交叉熵计算损失值
				求导数（求导只能用float型）
				更新w，b

## 四、项目工程
   1. 一些小知识：
		判定是否支持GPU
        	self.CUDA = torch.cuda.is_available()
		放到GPU的东西:
			模型权重参数
			训练集数据	
			测试集数据
				最后的下标值和概率值还是要返还给CPU
		模型的保存：
			os 目录保存
			#获取模块的安装路径
			current_dir = os.path.dirname(__file__)
			...
			self.mod_file = os.path.join(current_dir,"mods/lenet5.pt")
			(无论安装到哪都能找到这个绝对路径)

   2. YOLO训练
		1.基本的目录结构：
			01.models.py	核心
			02.utils		类和功能函数
			03.cfg/yolov4_ting.cfg	神经网络模型		Netron	
			04.datasets : 制作自己的数据集
			05.weights/yolov4-tiny.pt	初始化权重
			----------------------------------------------
			06.训练：train.py		run_train.bat
			07.测试和验证：test.py	run_train.bat
			08.侦测效果：detect.py	run_detect.bat
		2.定制数据集训练
		3.封装推理模型

		---------------
		
		训练两个模型：人脸模型/垃圾识别模型
		人脸模型：
			1.收集图片
			2.精灵标注助手标注（英文）
			3.json导出
			4.format检查
			5.datasets数据集建立（目录建立）
			|	faces.data
				│   faces.names
				│   train.txt
				│   valid.txt
				│
				└───faces
			    		├───images
			    		│   	└───train
			    		└───labels
			        			└───train
			6.拷贝图像
			7.faces.names	标签中的名
			   faces.data	仿写就行
			   train.txt		程序编写输出有顺序的文本
				
			   cfg:yolo4-tiny.cfg	classes=4 filters=（5 + 类别数）* 3

   3. API封装
		FaceDetector类中要实现的功能：
		1.图片预处理		pre_image
		2.图像侦测(基于训练模型)	yolo4_det
		3.返回有标注的图像		detect_mark
		4.返回标注的名字		get_name

		python setup.py install
		从此，调用库，创建对象，调用函数就能实现识别人脸

   4. 人脸登录的实现：
		1.推理模型已经安装到python,需要时调用库即可
		2.两个窗体：guis中的：garbagehome ,	facelogin
			先展示登录窗体	主窗体一直隐藏
			找路径	help(类)：可以更清楚地理解
		3.qt界面变为py文件：
			在路径下：pyuic5 -o loginui.py login.ui
		4.窗口大小固定：Login.setFixedSize(800, 520)
		5.摄像头采集图像：
			一直采集，直到采集到人脸，bool值 is_ok 才发生变化
			将采集到的信息以信号 signal_face 的形式一直 emit 被窗口处理后显示
			学会：合理地设置变量(全局/局部)；优雅地关闭线程
		    加入人工智能部分：加入数据验证模块(biz->login->user.py

   5.垃圾识别的实现同上：
		1.另外实现抓取图片和业务识别的能力