from distutils.core import setup

setup(
    name="garbageapp",
    version="1.0",
    description="应用程序",
    author=["Martin maxinyu",
        "Jim zhangjiawei",
        "Jack likang",
        "Syrson luoxiao"],
    packages=[
        "garbageapp",
        "garbageapp.biz",
        "garbageapp.devs",
        "garbageapp.guis",
        "garbageapp.biz.garbage",
        "garbageapp.biz.login",
        "garbageapp.devs.garbage",
        "garbageapp.devs.login",
        "garbageapp.guis.garbage",
        "garbageapp.guis.login",
    ],

    package_data={
        "garbageapp.guis.garbage":[
            "bilibili.jpg"
        ],
        "garbageapp.guis.login":[
            "22.jpg",
            "33.jpg",
            "222.jpg",
            "333.jpg",
            "login.ui"
        ],
    },

    scripts=["run_app.bat"]
)