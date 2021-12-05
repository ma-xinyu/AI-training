from  distutils.core import setup

setup(
    name="bigapp",
    version="1.0",
    description="面向对象的演示案例",
    author="martin",
    packages=[     # 目安装路径：${PYTHON/Lib/site-packages/}
        "bigapp",
        "bigapp.ais",
        "bigapp.uis"
    ],
    scripts=["run_app.bat"]  # ${PYTHON_HOME/Scripts}
)