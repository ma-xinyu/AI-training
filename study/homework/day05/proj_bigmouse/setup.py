from distutils.core import setup

setup(
    name="bigapp",
    version="1.0",
    description="演示案例",
    author="martin",
    packages=[      #目标安装路径：${PYTHON/Lib/site-packages}
        "bigapp",
        "bigapp,ais",
        "bigapp.uis",
    ],
    scripts=["run_app.bat"] #脚本 exe ${PYTHON_HOME/Scripts}
    #package_data=[]

)